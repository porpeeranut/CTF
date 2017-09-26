package oks;

import java.util.Enumeration;
import java.util.Hashtable;

import org.bouncycastle.asn1.ASN1Sequence;
import org.bouncycastle.asn1.DERObject;
import org.bouncycastle.asn1.DERObjectIdentifier;
import org.bouncycastle.asn1.DERSequence;
import org.bouncycastle.asn1.DERTaggedObject;
import org.bouncycastle.asn1.DERUTF8String;

public class ExtraProcessor {
	
	private static final String LEVEL1="1.2.840.113549.1.12.10.1.5";
	
	// extended by Tjado Mäcke 
	private static final String LEVEL2_1="2.16.840.1.113894.2.99.300.1";
	private static final String LEVEL2_2="1.2.840.113549.1.16.12.12";
	
	public Hashtable<String, String> data;
	
	private boolean inLevel1;
	private boolean inLevel2;
	
	public ExtraProcessor() {
		data=new Hashtable<String,String>();
	}
	
	public void process(DERObject d) {

		if (d instanceof DERSequence) {
			_processDSEQ((DERSequence)d);
        }		
	}
	
	private void _processDTO(DERTaggedObject dto) {
//		System.out.println("DERTaggedObject");
		Object o=dto.getObject();
		if (o!=null) {
			if (o instanceof DERSequence) {
				_processDSEQ((DERSequence)o);
			}
		}
	}
	private void _processDSEQ(DERSequence d) {
//		System.out.println("DERSequence");
        Enumeration e = ((ASN1Sequence)d).getObjects();

        while (e.hasMoreElements()) {
            Object  o = e.nextElement();            
            if (o instanceof DERObjectIdentifier) {
            	DERObjectIdentifier dto=(DERObjectIdentifier)o;
            	String id=dto.getId();
            	if (id.equals(LEVEL1)) inLevel1=true;
            	if (id.equals(LEVEL2_1)) inLevel2=true;
            	if (id.equals(LEVEL2_2)) inLevel2=true;
            }
            if (o instanceof DERTaggedObject) {
            	_processDTO((DERTaggedObject)o);
            }
            if (o instanceof DERUTF8String) {
            	if ((inLevel1) && (inLevel2)) {
            		DERUTF8String key=(DERUTF8String)o;
            		DERUTF8String value=(DERUTF8String)(e.nextElement());
            		data.put(key.getString(), value.getString());
            	}
            }
            else {
//            	System.out.println(o.getClass());
            }
        }
        
        if (inLevel2) inLevel2=false;
        else if (inLevel1) inLevel1=false;
	}
}

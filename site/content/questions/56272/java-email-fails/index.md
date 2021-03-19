+++
type = "question"
title = "[closed] Java email fails"
description = '''My java application is unable to send emails but when I restart the server it will again send emails for 3 to 4 days and again the same issue repeats and throws connection refused and couldn&#x27;t connect to smtp localhost 465 package com.fps.mail; import java.util.ArrayList; import java.util.Iterator; ...'''
date = "2016-10-09T22:42:00Z"
lastmod = "2016-10-09T22:42:00Z"
weight = 56272
keywords = [ "offtopic", "smtp" ]
aliases = [ "/questions/56272" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Java email fails](/questions/56272/java-email-fails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56272-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My java application is unable to send emails but when I restart the server it will again send emails for 3 to 4 days and again the same issue repeats and throws connection refused and couldn't connect to smtp localhost 465</p><p>package com.fps.mail;</p><p>import java.util.ArrayList; import java.util.Iterator; import java.util.List; import java.util.Properties;</p><p>import javax.activation.DataHandler; import javax.activation.FileDataSource; import javax.mail.Address; import javax.mail.Message; import javax.mail.MessagingException; import javax.mail.Multipart; import javax.mail.PasswordAuthentication; import javax.mail.Session; import javax.mail.Transport; import javax.mail.internet.AddressException; import javax.mail.internet.InternetAddress; import javax.mail.internet.MimeBodyPart; import javax.mail.internet.MimeMessage; import javax.mail.internet.MimeMultipart;</p><p>import com.fps.exceptions.SystemException; import com.fps.utils.Constants; import com.fps.utils.HelperFunctions; import com.fps.utils.LogHelper;</p><p>/* <em>* A singleton thread that handles all the mailings within the project. * All mails are sent asynchronously, at specific intervals *<br />
* Contains wrapper methods to send mail using the Java Mail API.</em> /</p><p>/ <em>* Modification Log: (mm/dd/yyyy [Author] Changes) * * 03/16/2004 [Rahul Gedupudi] Base Version * 04/05/2007 [Sunitha Venkataraman] Updated to JDK 1.5 - Parameterized List</em> /</p><p>public class MailHandler implements Runnable {</p><pre><code>//singleton variable
private static MailHandler instance = new MailHandler();

//contains a list of MailDetail objects representing all the mails that have to be sent
private List&lt;Object&gt; mails = null;

//interval after which the thread checks to send mails
//currently at 10 mins
private static final long INTERVAL = 60000;

//contains the properties to be used for obtaining mail session
private Properties mailProps = null;

/**
 * Private Constructor. Use getInstance().
 */
private MailHandler() {
    super();

    this.mails = new ArrayList&lt;Object&gt;(1);

    //setup mail server properties
    this.mailProps = System.getProperties();
    this.mailProps.put(Constants.MAIL_PROP, Constants.MAIL_HOST);
    this.mailProps.put(&quot;mail.smtp.socketFactory.port&quot;, &quot;465&quot;);
    this.mailProps.put(&quot;mail.smtp.socketFactory.class&quot;,&quot;javax.net.ssl.SSLSocketFactory&quot;);
    this.mailProps.put(&quot;mail.smtp.auth&quot;, &quot;true&quot;);
    this.mailProps.put(&quot;mail.smtp.port&quot;, &quot;465&quot;);

    //this.mailProps.put(&quot;mail.smtp.starttls.enable&quot;,&quot;true&quot;);       
    /*this.mailProps.put(&quot;mail.smtp.port&quot;, &quot;25&quot;);
    this.mailProps.put(&quot;mail.smtp.EnableSsl&quot;, &quot;false&quot;);*/
    /*this.mailProps.put(&quot;mail.smtp.socketFactory.port&quot;, &quot;25&quot;); 
    this.mailProps.put(&quot;mail.smtp.socketFactory.fallback&quot;, &quot;false&quot;);*/

    //this.mailProps.put(&quot;mail.debug&quot;, &quot;true&quot;);

    //start a thread        
    Thread mailThread = new Thread(this);
    mailThread.start();
} //end constructor

/**
 * Gets the instance
 * @return Returns a MailHelper
 */
public static MailHandler getInstance() {
    return instance;
} //end getInstance

/**
 * add a mail detail object to the mails list
 */
public void addMail(MailDetail _mailDetail) {
    synchronized (this.mails) {
        this.mails.add(_mailDetail);
    }
} //end addMail

/**
 * used by the thread to send e-mails at set intervals
 */
public void run() {
    while (true) {
        //create a new list out of the mails list, and empty out mails list
        //this is needed to prevent concurrent access modification exceptions.
        List&lt;Object&gt; tempList = null;
        synchronized (this.mails) {
            tempList = new ArrayList&lt;Object&gt;(this.mails);
            this.mails.clear();
        }

        //move to the top of the iterator
        Iterator&lt;Object&gt; iter = tempList.iterator();
        //check the e-mail list, and send mails if present
        while (iter.hasNext()) {
            boolean mailError = false;
            MailDetail mailDetail = (MailDetail) iter.next();
            try {
                this.sendMail(mailDetail);
            }
            catch (SystemException se) {
                LogHelper.getInstance().errorMessage(this, null, &quot;Error sending e-mail&quot;, se);
                mailError = true;
            }

            //if there is no mail error, delete this MailDetail object, so it is not sent again
            if (!mailError) {
                iter.remove();
            }
        } //end while

        //if there are any elements in tempList, add it back to mails list to be taken care of in the next iteration
        if (!tempList.isEmpty()) {
            for (int i = 0, size = tempList.size(); i &lt; size; i++)
                this.addMail((MailDetail) tempList.get(i));
        }

        try {
            Thread.sleep(INTERVAL); //sleep for interval time
        }
        catch (InterruptedException ie) {
            //ignore
        }
    } //end while
} //end run

/**
 * Helper method that returns an object of type InternetAddress from the passed email address string.
 * &lt;br&gt;
 * The boolean variable _from specifies whether this address is for the &quot;From&quot; part of the mail.
 * If set to true, and the passed address is invalid, defaults the address to Constants.MAIL_DEF_ADDR
 */
private Address getEmailAddress(final String _emailAddr, boolean _from) {
    Address address = null;
    try {
        address = new InternetAddress(_emailAddr);
    }
    catch (AddressException ae) {
        LogHelper.getInstance().errorMessage(this, null, &quot;Error trying to obtain mailing address: &quot; + _emailAddr);

        //if this method is called for a &quot;from&quot; address, send the default address
        if (_from) {
            try {
                address = new InternetAddress(Constants.MAIL_DEFAULT_ADDR);
            }
            catch (AddressException aex) {
                //ignore -- should not happen
            }
        }
    }

    return address;
} //end getEmailAddress

/**
 * Helper method that sends a mail message.
 */
private void sendMail(MailDetail _mailDetail) throws SystemException {
    if ((_mailDetail.getToAddresses() == null) || _mailDetail.getToAddresses().isEmpty())
        throw new SystemException(&quot;Trying to send mail to an empty address list&quot;);

    //if there is no from address, use the default address
    if (HelperFunctions.isEmpty(_mailDetail.getFromAddress(), true)) {
        LogHelper.getInstance().warningMessage(this, null, &quot;Trying to send mail with an empty &#39;to&#39; address&quot;);
        _mailDetail.setFromAddress(Constants.MAIL_DEFAULT_ADDR);
    }

    //get the session
    Session session = Session.getInstance(this.mailProps, new SMTPAuthenticator());

    //define message
    MimeMessage message = new MimeMessage(session);

    //set the &#39;from&#39; address
    Address fromAddr = this.getEmailAddress(_mailDetail.getFromAddress(), true);
    //fromAddr should never be null, as it will contain at least the default address
    try {
        message.setFrom(fromAddr);
    }
    catch (MessagingException me) {
        throw new SystemException(&quot;Invalid &#39;from&#39; Address: &quot; + _mailDetail.getFromAddress(), me, false);
    }

    //set the &#39;to&#39; addresses
    for (int i = 0, size = _mailDetail.getToAddresses().size(); i &lt; size; i++) {
        Address toAddr = this.getEmailAddress((String) _mailDetail.getToAddresses().get(i), false);
        if (toAddr != null)
            try {
                message.addRecipient(Message.RecipientType.TO, toAddr);
            }
        catch (MessagingException me) {
            throw new SystemException(&quot;Invalid &#39;to&#39; address: &quot; + _mailDetail.getToAddresses().get(i), me, false);
        }
    } //end for

    //set the &#39;cc&#39; addresses, if present
    if (_mailDetail.getCcAddresses() != null)
        for (int i = 0, size = _mailDetail.getCcAddresses().size(); i &lt; size; i++) {
            Address ccAddr = this.getEmailAddress((String) _mailDetail.getCcAddresses().get(i), false);
            if (ccAddr != null)
                try {
                    message.addRecipient(Message.RecipientType.CC, ccAddr);
                }
            catch (MessagingException me) {
                throw new SystemException(&quot;Invalid &#39;cc&#39; address: &quot; + _mailDetail.getCcAddresses().get(i), me, false);
            }
        } //end for

        //set the &#39;bcc&#39; addresses
    if (_mailDetail.getBccAddresses() != null)
        for (int i = 0, size = _mailDetail.getBccAddresses().size(); i &lt; size; i++) {
            Address bccAddr = this.getEmailAddress((String) _mailDetail.getBccAddresses().get(i), false);
            if (bccAddr != null)
                try {
                    message.addRecipient(Message.RecipientType.BCC, bccAddr);
                }
            catch (MessagingException me) {
                throw new SystemException(&quot;Invalid &#39;bcc&#39; address: &quot; + _mailDetail.getBccAddresses().get(i), me, false);
            }
        } //end for

        //set the subject
    try {
        if (_mailDetail.getSubject() != null)
            message.setSubject(_mailDetail.getSubject());
    }
    catch (MessagingException me) {
        throw new SystemException(&quot;Error setting subject: &quot; + _mailDetail.getSubject(), me, false);
    }

    //set the text and attachments
    try {
        Multipart mp = new MimeMultipart();

        //add text
        MimeBodyPart textPart = new MimeBodyPart();
        if (_mailDetail.getText() != null)
            textPart.setContent(_mailDetail.getText(), _mailDetail.getMailType());
        else
            textPart.setContent(&quot;&quot;, MailDetail.TEXT_MAIL);
        mp.addBodyPart(textPart);

        //add attachments
        if (_mailDetail.getAttachments() != null &amp;&amp; !_mailDetail.getAttachments().isEmpty())
            for (int i = 0, size = _mailDetail.getAttachments().size(); i &lt; size; i++) {
                MimeBodyPart attachFilePart = new MimeBodyPart();
                FileDataSource fds = new FileDataSource((String) _mailDetail.getAttachments().get(i));
                attachFilePart.setDataHandler(new DataHandler(fds));
                attachFilePart.setFileName(fds.getName());
                mp.addBodyPart(attachFilePart);
            }

        message.setContent(mp);
    }
    catch (MessagingException me) {
        throw new SystemException(&quot;Error setting text: &quot; + _mailDetail.getText(), me, false);
    }

    //send message
    try {
        Transport.send(message);
    }
    catch (MessagingException me) {
        throw new SystemException(&quot;Error sending e-mail message.&quot;, me, false);
    }
} //end sendMail

private class SMTPAuthenticator extends javax.mail.Authenticator
{
    public PasswordAuthentication getPasswordAuthentication()
    {

        //return new PasswordAuthentication(&quot;&quot;, &quot;&quot;);
    }
}</code></pre><p>} //end class</p></div><div id="question-tags" class="tags-container tags">offtopic smtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '16, 22:42</strong></p><img src="https://secure.gravatar.com/avatar/073d0258cb92d45def2ee713ac2d05ae?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Srinivas%20Yadadadad&#39;s gravatar image" /><p>Srinivas Yad...<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Srinivas Yadadadad has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>closed 10 Oct '16, 01:16</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-56272" class="comments-container"></div><div id="comment-tools-56272" class="comment-tools"></div><div class="clear"></div><div id="comment-56272-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant. This is a Wireshark Q&A, including packet capture/network analysis. Maybe http://stackoverflow.com/questions/tagged/java is a better place for this." by Jasper 10 Oct '16, 01:16

</div>

</div>

</div>


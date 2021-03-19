+++
type = "question"
title = "How to add an xml file to the Diameter dictionary"
description = '''Hi, I have below AVP&#x27;s added in avp.xml  &amp;lt;avp name=&quot;Subscriber_Category&quot; code=&quot;1003&quot; vendor-id=&quot;Comviva&quot; mandatory=&quot;must&quot; protected=&quot;mustnot&quot; may-encrypt=&quot;yes&quot; vendor-bit=&quot;must&quot;&amp;gt; &amp;lt;type type-name=&quot;Unsigned32&quot;/&amp;gt;  &amp;lt;/avp&amp;gt; still i am getting AVP as unknown . I am using tshark to read pc...'''
date = "2014-09-10T06:50:00Z"
lastmod = "2014-09-11T06:05:00Z"
weight = 36166
keywords = [ "diameter", "avp", "dictionary" ]
aliases = [ "/questions/36166" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to add an xml file to the Diameter dictionary](/questions/36166/how-to-add-an-xml-file-to-the-diameter-dictionary)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36166-score" class="post-score" title="current number of votes">0</div><span id="post-36166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have below AVP's added in avp.xml</p><p>&lt;avp name="Subscriber_Category" code="1003" vendor-id="Comviva" mandatory="must" protected="mustnot" may-encrypt="yes" vendor-bit="must"&gt; &lt;type type-name="Unsigned32"/&gt; &lt;/avp&gt;</p><p>still i am getting AVP as unknown .</p><p>I am using tshark to read pcap and am using -z for diameter protocol . i am unable to get that AVP as it is a unknown AVP .</p><p>will tshark supports AVP's of Vendor other than 3GPP?</p><p>BR, Ankamma</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-avp" rel="tag" title="see questions tagged &#39;avp&#39;">avp</span> <span class="post-tag tag-link-dictionary" rel="tag" title="see questions tagged &#39;dictionary&#39;">dictionary</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Sep '14, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/eee0a26e9a44f674f864f2525b82efb9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankamma&#39;s gravatar image" /><p><span>ankamma</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankamma has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Sep '14, 06:05</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-36166" class="comments-container"><span id="36176"></span><div id="comment-36176" class="comment"><div id="post-36176-score" class="comment-score"></div><div class="comment-text"><p>hi ,</p><p>i have two files dictionary,vendor_avp.xml .</p><p>dictionary file is like below:</p><p># # Vendor-Specific attributes use the SMI Network Management Private # Enterprise Code from the "Assigned Numbers" RFC (currently RFC 1700) # # # You need to activate a VSA mode on your box to get these attributes # in accounting records #</p><pre><code>VENDOR          3GPP            10415
ATTRIBUTE       3GPP-IMSI                                          1        string         3GPP
ATTRIBUTE       3GPP-ChargingID                                         2        integer        3GPP
ATTRIBUTE       3GPP-PDPType                                            3        integer        3GPP
ATTRIBUTE       3GPP-Charging-Gateway-Address                           4        string         3GPP
ATTRIBUTE       3GPP-SGSN-Address                                       6        ipaddr         3GPP
ATTRIBUTE       3GPP-GGSN-Address                                       7        ipaddr         3GPP
ATTRIBUTE       3GPP-IMSI-MCC-MNC                                       8        string         3GPP
ATTRIBUTE       3GPP-GGSN-MCC-MNC                                       9        string         3GPP
ATTRIBUTE       3GPP-NSAPI                                                      10       string         3GPP</code></pre><p>and vendor_avp.xml is like below:</p><pre><code>&lt;dictionary&gt;
&lt;base uri=&quot;http://www.ietf.org/rfc/rfc3588.txt&quot;&gt;
    &lt;vendor vendor-id=&quot;3gpp&quot; code=&quot;10415&quot; name=&quot;ietf&quot;/&gt;
    &lt;vendor vendor-id=&quot;Comviva&quot; code=&quot;40136&quot; name=&quot;Comviva&quot;/&gt;
    &lt;vendor vendor-id=&quot;Ericsson&quot; code=&quot;193&quot; name=&quot;Ericsson&quot;/&gt;
&lt;vendor vendor-id=&quot;Cisco&quot; code=&quot;9&quot; name=&quot;Cisco&quot;/&gt;
    &lt;vendor name=&quot;Huawei&quot; code=&quot;2011&quot; vendor-id=&quot;Huawei&quot;/&gt;
&lt;vendor vendor-id=&quot;ietf&quot; code=&quot;0&quot; name=&quot;ietf&quot;/&gt;
&lt;/base&gt;

&lt;application id=&quot;16777238&quot; name=&quot;3GPP Gx&quot; uri=&quot;&quot;&gt;

            &lt;!-- Comviva Starts  --&gt;

            &lt;avp name=&quot;Comviva-Package_ID&quot; code=&quot;1001&quot; vendor-id=&quot;Comviva&quot; mandatory=&quot;mustnot&quot; protected=&quot;mustnot&quot; may-encrypt=&quot;yes&quot; vendor-bit=&quot;must&quot;&gt;
                    &lt;type type-name=&quot;UTF8String&quot;/&gt;
            &lt;/avp&gt;

             &lt;avp name=&quot;Parent_NAI&quot; code=&quot;1002&quot; vendor-id=&quot;Comviva&quot; mandatory=&quot;mustnot&quot; protected=&quot;mustnot&quot; may-encrypt=&quot;yes&quot; vendor-bit=&quot;must&quot;&gt;
             &lt;type type-name=&quot;UTF8String&quot;/&gt;
             &lt;/avp&gt;</code></pre><p>please let me know where to add Entity exactly. please share give me your mail id so that i can mail complete files.</p><p>BR, Ankamma</p></div><div id="comment-36176-info" class="comment-info"><span class="comment-age">(10 Sep '14, 09:34)</span> <span class="comment-user userinfo">ankamma</span></div></div><span id="36179"></span><div id="comment-36179" class="comment"><div id="post-36179-score" class="comment-score">1</div><div class="comment-text"><p>Look in dictionary.xml at the other files that are loaded into it. For example, these are the lines relevant to loading SKT.xml:</p><pre><code>    &lt;!ENTITY SKT            SYSTEM &quot;SKT.xml&quot;&gt;
[...]
&amp;SKT;</code></pre></div><div id="comment-36179-info" class="comment-info"><span class="comment-age">(10 Sep '14, 11:09)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-36166" class="comment-tools"></div><div class="clear"></div><div id="comment-36166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36170"></span>

<div id="answer-container-36170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36170-score" class="post-score" title="current number of votes">1</div><span id="post-36170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To add a new .xml file you neeed to update the ENTITY list in dictionaty.xml and also add it at the bottom of the file( Compare with say HP.xml) For the vendor-id You need to add Comviva to the vendor list.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-36170" class="comments-container"><span id="36191"></span><div id="comment-36191" class="comment"><div id="post-36191-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>by adding below lines it is working fine and am able to get AVP names in wireshark(windows).</p><p>but how to achieve the same in tshark(linux)? where to add Entity in Linux?</p><p>[<span class="__cf_email__" data-cfemail="15677a7a6155747b7e74787874">[email protected]</span> tmp]# tshark -r /tmp/Gx_dump1.pcap -d 'tcp.port==3870,diameter' -R "diameter.cmd.code==272 and diameter.flags.request==0" -z "diameter,avp,272,CC-Request-Type,CC-Request-Number,Session-Id,Subscription-Id-Data,Rating-Group,Result-Code,Session-Id,Custom_Result_Code" tshark: -R without -2 is deprecated. For single-pass filtering use -Y. tshark: Couldn't register diam,csv tap: Filter "diameter||diameter.CC-Request-Type||diameter.CC-Request-Number||diameter.Session-Id||diameter.Subscription-Id-Data||diameter.Rating-Group||diameter.Result-Code||diameter.Session-Id||diameter.Custom_Result_Code" is invalid - "diameter.Custom_Result_Code" is neither a field nor a protocol name.</p><p>BR, Ankamma</p></div><div id="comment-36191-info" class="comment-info"><span class="comment-age">(10 Sep '14, 23:06)</span> <span class="comment-user userinfo">ankamma</span></div></div><span id="36192"></span><div id="comment-36192" class="comment"><div id="post-36192-score" class="comment-score"></div><div class="comment-text"><p>hi,</p><p>i got it working by adding entity in the same way</p></div><div id="comment-36192-info" class="comment-info"><span class="comment-age">(10 Sep '14, 23:16)</span> <span class="comment-user userinfo">ankamma</span></div></div><span id="36202"></span><div id="comment-36202" class="comment"><div id="post-36202-score" class="comment-score"></div><div class="comment-text"><p>Glad you got it working.</p><p>If an Answer answers your question, please Accept the answer by clicking on the little checkbox next to it. See the FAQ for details.</p></div><div id="comment-36202-info" class="comment-info"><span class="comment-age">(11 Sep '14, 06:05)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-36170" class="comment-tools"></div><div class="clear"></div><div id="comment-36170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


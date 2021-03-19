+++
type = "question"
title = "tshark and uat:user_dlts"
description = '''Hi all, according with link text, I&#x27;m trying to parse a .pcap.uat file tshark -o &quot;uat:user_dlts:&#92;&quot;User 15 (DLT=162)&#92;&quot;,&#92;&quot;pcap&#92;&quot;,&#92;&quot;0&#92;&quot;,&#92;&quot;&#92;&quot;,&#92;&quot;0&#92;&quot;,&#92;&quot;&#92;&quot;&quot; &#92;  -o &quot;uat:user_dlts:&#92;&quot;User 15 (DLT=162)&#92;&quot;,&#92;&quot;mtp3&#92;&quot;,&#92;&quot;12&#92;&quot;,&#92;&quot;&#92;&quot;,&#92;&quot;0&#92;&quot;,&#92;&quot;&#92;&quot;&quot;   -nr test.pcap.uat -T pdml &amp;gt; test.xml  FILE: link text The result is  ...'''
date = "2013-10-10T05:33:00Z"
lastmod = "2013-10-14T03:08:00Z"
weight = 25869
keywords = [ "tshark", "uat" ]
aliases = [ "/questions/25869" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [tshark and uat:user\_dlts](/questions/25869/tshark-and-uatuser_dlts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25869-score" class="post-score" title="current number of votes">0</div><span id="post-25869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, according with <a href="http://ask.wireshark.org/questions/24474/user_dlt-option-in-tshark">link text</a>, I'm trying to parse a .pcap.uat file</p><pre><code>tshark -o &quot;uat:user_dlts:\&quot;User 15 (DLT=162)\&quot;,\&quot;pcap\&quot;,\&quot;0\&quot;,\&quot;\&quot;,\&quot;0\&quot;,\&quot;\&quot;&quot; \
   -o &quot;uat:user_dlts:\&quot;User 15 (DLT=162)\&quot;,\&quot;mtp3\&quot;,\&quot;12\&quot;,\&quot;\&quot;,\&quot;0\&quot;,\&quot;\&quot;&quot; 
   -nr test.pcap.uat       -T pdml &gt; test.xml</code></pre><p>FILE: <a href="http://speedy.sh/TvR4R/test.pcap.uat.pcap">link text</a></p><p>The result is <code> &lt;packet&gt;   &lt;proto name="geninfo" pos="0" showname="General information" size="106"&gt;     &lt;field name="num" pos="0" show="1" showname="Number" value="1" size="106"/&gt;     &lt;field name="len" pos="0" show="106" showname="Frame Length" value="6a" size="106"/&gt;     &lt;field name="caplen" pos="0" show="106" showname="Captured Length" value="6a" size="106"/&gt;     &lt;field name="timestamp" pos="0" show="Oct 10, 2013 12:22:15.885200000" showname="Captured Time" value="1381400535.885200000" size="106"/&gt;   &lt;/proto&gt;   &lt;proto name="frame" showname="Frame 1 (106 bytes on wire, 106 bytes captured)" size="106" pos="0"&gt;   ...   &lt;/proto&gt;   &lt;proto name="user_dlt" showname="DLT: 162" size="0" pos="0"/&gt;   &lt;proto name="fake-field-wrapper"&gt; ----------------------&gt; Decoding Error!!!     &lt;field name="data" value="000100046d7470330002005e"/&gt;       &lt;field name="data.data" showname="Data: 000100046D7470330002005E" size="12" pos="0" show="00:01:00:04:6d:74:70:33:00:02:00:5e" value="000100046d7470330002005e"/&gt;       &lt;field name="data.len" showname="Length: 12" size="0" pos="0" show="12"/&gt;   &lt;/proto&gt;</code></p><p>In Wireshark (windows), the same approach in preferences-protocols-user dlts works...</p><p>How can I add multiple uat:user_dlts?</p><p>Thanks Riccardo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-uat" rel="tag" title="see questions tagged &#39;uat&#39;">uat</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '13, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/a5626909eb9fd5bbf9e3ac3861076738?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ric79&#39;s gravatar image" /><p><span>Ric79</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ric79 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Oct '13, 22:30</strong> </span></p></div></div><div id="comments-container-25869" class="comments-container"></div><div id="comment-tools-25869" class="comment-tools"></div><div class="clear"></div><div id="comment-25869-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25914"></span>

<div id="answer-container-25914" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25914-score" class="post-score" title="current number of votes">1</div><span id="post-25914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ric79 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>In Wireshark (windows), the same approach in preferences-protocols-user dlts works...<br />
How can I add multiple uat:user_dlts?</p></blockquote><p>The order of the USR_DLT definition is important. In the GUI you can move definitions with the UP/DOWN buttons. The first definition that matches will be taken. So, If I <strong>first</strong> define DLT=162 in the GUI as MTP3, the frame gets fully dissected. If I <strong>first</strong> define DLT=162 as PCAP, there is an error, which is obvious, as the file does not contain the right structure.</p><p>The same is true for tshark. The order of the -o options is important. If you reverse the order in your example (first mtp3, then pcap), the MTP3 data in the file will be dissected as MTP3. However, <strong>it does not make sense to define the same USR_DLT twice in tshark</strong>, as only the first matching USR_DLT will be used.</p><p><strong>In the GUI</strong> however, it <strong>might make sense</strong>, as the definitions can be prepared in advance. Then, if you need a different definition, you move up the one you need, until it is the first definition.</p><p>Example: mtp3 first (although the second definition does not make sense - see above)</p><blockquote><p>tshark -nr usr_dlt.pcap -o "uat:user_dlts:\"User 15 (DLT=162)\",\"<strong>mtp3</strong>\",\"12\",\"\",\"0\",\"\"" -o "uat:user_dlts:\"User 15 (DLT=162)\",\"pcap\",\"0\",\"\",\"0\",\"\"" -T pdml</p></blockquote><p>Output:</p><pre><code>

&lt;pdml version=&quot;0&quot; creator=&quot;wireshark/1.10.2&quot; time=&quot;Fri Oct 11 14:07:00 2013&quot; capture_file=&quot;usr_dlt.pcap&quot;&gt;
&lt;packet&gt;
  &lt;proto name=&quot;geninfo&quot; pos=&quot;0&quot; showname=&quot;General information&quot; size=&quot;44&quot;&gt;
    &lt;field name=&quot;num&quot; pos=&quot;0&quot; show=&quot;1&quot; showname=&quot;Number&quot; value=&quot;1&quot; size=&quot;44&quot;/&gt;
    &lt;field name=&quot;len&quot; pos=&quot;0&quot; show=&quot;44&quot; showname=&quot;Frame Length&quot; value=&quot;2c&quot; size=&quot;44&quot;/&gt;
    &lt;field name=&quot;caplen&quot; pos=&quot;0&quot; show=&quot;44&quot; showname=&quot;Captured Length&quot; value=&quot;2c&quot; size=&quot;44&quot;/&gt;
    &lt;field name=&quot;timestamp&quot; pos=&quot;0&quot; show=&quot;Oct 10, 2013 12:22:15.907100000 WesteuropÃ¤ische Sommerzeit&quot; showname=&quot;Captured Time&quot; value=&quot;13814
00535.907100000&quot; size=&quot;44&quot;/&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;frame&quot; showname=&quot;Frame 1: 44 bytes on wire (352 bits), 44 bytes captured (352 bits)&quot; size=&quot;44&quot; pos=&quot;0&quot;&gt;
    &lt;field name=&quot;frame.encap_type&quot; showname=&quot;Encapsulation type: USER 15 (60)&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;60&quot;/&gt;
    &lt;field name=&quot;frame.time&quot; showname=&quot;Arrival Time: Oct 10, 2013 12:22:15.907100000 Westeurop\xc3\xa4ische Sommerzeit&quot; size=&quot;0&quot; pos=&quot;0&quot; sho=&quot;&quot; w=&quot;Oct 10, 2013 12:22:15.907100000&quot;/&gt;
    &lt;field name=&quot;frame.offset_shift&quot; showname=&quot;Time shift for this packet: 0.000000000 seconds&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;0.000000000&quot;/&gt;
    &lt;field name=&quot;frame.time_epoch&quot; showname=&quot;Epoch Time: 1381400535.907100000 seconds&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;1381400535.907100000&quot;/&gt;
    &lt;field name=&quot;frame.time_delta&quot; showname=&quot;Time delta from previous captured frame: 0.000000000 seconds&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;0.00000000
0&quot;/&gt;
    &lt;field name=&quot;frame.time_delta_displayed&quot; showname=&quot;Time delta from previous displayed frame: 0.000000000 seconds&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;0.000000000&quot;/&gt;
    &lt;field name=&quot;frame.time_relative&quot; showname=&quot;Time since reference or first frame: 0.000000000 seconds&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;0.000000000
&quot;/&gt;
    &lt;field name=&quot;frame.number&quot; showname=&quot;Frame Number: 1&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;1&quot;/&gt;
    &lt;field name=&quot;frame.len&quot; showname=&quot;Frame Length: 44 bytes (352 bits)&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;44&quot;/&gt;
    &lt;field name=&quot;frame.cap_len&quot; showname=&quot;Capture Length: 44 bytes (352 bits)&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;44&quot;/&gt;
    &lt;field name=&quot;frame.marked&quot; showname=&quot;Frame is marked: False&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;0&quot;/&gt;
    &lt;field name=&quot;frame.ignored&quot; showname=&quot;Frame is ignored: False&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;0&quot;/&gt;
    &lt;field name=&quot;frame.protocols&quot; showname=&quot;Protocols in frame: user_dlt:data:mtp3:sccp:ranap&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;user_dlt:data:mtp3:scc
p:ranap&quot;/&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;user_dlt&quot; showname=&quot;DLT: 162, Payload: mtp3 (Message Transfer Part Level 3)&quot; size=&quot;44&quot; pos=&quot;0&quot;/&gt;
  &lt;proto name=&quot;fake-field-wrapper&quot;&gt;
    &lt;field name=&quot;data&quot; value=&quot;000100046d74703300020020&quot;&gt;
      &lt;field name=&quot;data.data&quot; showname=&quot;Data: 000100046d74703300020020&quot; size=&quot;12&quot; pos=&quot;0&quot; show=&quot;00:01:00:04:6d:74:70:33:00:02:00:20&quot; value=&quot;
000100046d74703300020020&quot;/&gt;
      &lt;field name=&quot;data.len&quot; showname=&quot;Length: 12&quot; size=&quot;0&quot; pos=&quot;0&quot; show=&quot;12&quot;/&gt;
  &lt;/field&gt;
&lt;/proto&gt;
  &lt;proto name=&quot;mtp3&quot; showname=&quot;Message Transfer Part Level 3&quot; size=&quot;5&quot; pos=&quot;12&quot;&gt;
    &lt;field name=&quot;&quot; show=&quot;Service information octet&quot; size=&quot;1&quot; pos=&quot;12&quot; value=&quot;c3&quot;&gt;
      &lt;field name=&quot;mtp3.network_indicator&quot; showname=&quot;11.. .... = Network indicator: Reserved for national use (0x03)&quot; size=&quot;1&quot; pos=&quot;12&quot; show=&quot;0x03&quot; value=&quot;3&quot; unmaskedvalue=&quot;c3&quot;/&gt;
      &lt;field name=&quot;mtp3.spare&quot; showname=&quot;..00 .... = Spare: 0x00&quot; size=&quot;1&quot; pos=&quot;12&quot; show=&quot;0x00&quot; value=&quot;0&quot; unmaskedvalue=&quot;c3&quot;/&gt;
      &lt;field name=&quot;mtp3.service_indicator&quot; showname=&quot;.... 0011 = Service indicator: SCCP (0x03)&quot; size=&quot;1&quot; pos=&quot;12&quot; show=&quot;0x03&quot; value=&quot;3&quot; unm=&quot;&quot; askedvalue=&quot;c3&quot;/&gt;
    &lt;/field&gt;
    &lt;field name=&quot;&quot; show=&quot;Routing label&quot; size=&quot;4&quot; pos=&quot;13&quot; value=&quot;319e7b31&quot;&gt;
      &lt;field name=&quot;mtp3.pc&quot; showname=&quot;PC: 1518&quot; hide=&quot;yes&quot; size=&quot;4&quot; pos=&quot;13&quot; show=&quot;1518&quot; value=&quot;319e7b31&quot;/&gt;
      &lt;field name=&quot;mtp3.pc&quot; showname=&quot;PC: 7729&quot; hide=&quot;yes&quot; size=&quot;4&quot; pos=&quot;13&quot; show=&quot;7729&quot; value=&quot;319e7b31&quot;/&gt;
      &lt;field name=&quot;mtp3.dpc&quot; showname=&quot;.... .... .... .... ..01 1110 0011 0001 = DPC: 7729&quot; size=&quot;4&quot; pos=&quot;13&quot; show=&quot;7729&quot; value=&quot;1E31&quot; unmas=&quot;&quot; kedvalue=&quot;319e7b31&quot;/&gt;
      &lt;field name=&quot;mtp3.opc&quot; showname=&quot;.... 0001 0111 1011 10.. .... .... .... = OPC: 1518&quot; size=&quot;4&quot; pos=&quot;13&quot; show=&quot;1518&quot; value=&quot;5EE&quot; unmask=&quot;&quot; edvalue=&quot;319e7b31&quot;/&gt;
      &lt;field name=&quot;mtp3.sls&quot; showname=&quot;0011 .... .... .... .... .... .... .... = Signalling Link Selector: 3&quot; size=&quot;4&quot; pos=&quot;13&quot; show=&quot;3&quot; val=&quot;&quot; ue=&quot;3&quot; unmaskedvalue=&quot;319e7b31&quot;/&gt;
    &lt;/field&gt;
  &lt;/proto&gt;
  &lt;proto name=&quot;sccp&quot; showname=&quot;Signalling Connection Control Part&quot; size=&quot;27&quot; pos=&quot;17&quot;&gt;
    &lt;field name=&quot;sccp.message_type&quot; showname=&quot;Message Type: Data Form 1 (0x06)&quot; size=&quot;1&quot; pos=&quot;17&quot; show=&quot;0x06&quot; value=&quot;06&quot;/&gt;
    &lt;field name=&quot;sccp.dlr&quot; showname=&quot;Destination Local Reference: 0x6f5a00&quot; size=&quot;3&quot; pos=&quot;18&quot; show=&quot;0x6f5a00&quot; value=&quot;005a6f&quot;/&gt;
    &lt;field name=&quot;sccp.lr&quot; showname=&quot;Local Reference: 0x6f5a00&quot; hide=&quot;yes&quot; size=&quot;3&quot; pos=&quot;18&quot; show=&quot;0x6f5a00&quot; value=&quot;005a6f&quot;/&gt;
    &lt;field name=&quot;sccp.more&quot; showname=&quot;.... ...0 = More data: No more data (0x00)&quot; size=&quot;1&quot; pos=&quot;21&quot; show=&quot;0x00&quot; value=&quot;0&quot; unmaskedvalue=&quot;00&quot;/&gt;
    &lt;field name=&quot;sccp.variable_pointer1&quot; showname=&quot;Pointer to first Mandatory Variable parameter: 1&quot; size=&quot;1&quot; pos=&quot;22&quot; show=&quot;1&quot; value=&quot;01&quot;/&gt;

  &lt;/proto&gt;
  &lt;proto name=&quot;ranap&quot; showname=&quot;Radio Access Network Application Part&quot; size=&quot;20&quot; pos=&quot;24&quot;&gt;
    &lt;field name=&quot;per.extension_bit&quot; showname=&quot;0... .... Extension Bit: False&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;24&quot; show=&quot;0&quot; value=&quot;0&quot; unmaskedvalue=&quot;00&quot;/&gt;
    &lt;field name=&quot;per.choice_index&quot; showname=&quot;Choice Index: 0&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;24&quot; show=&quot;0&quot; value=&quot;00&quot;/&gt;
    &lt;field name=&quot;ranap.RANAP_PDU&quot; showname=&quot;RANAP-PDU: initiatingMessage (0)&quot; size=&quot;20&quot; pos=&quot;24&quot; show=&quot;0&quot; value=&quot;000f40100000010017400950220
20000000000f0&quot;&gt;
      &lt;field name=&quot;ranap.initiatingMessage&quot; showname=&quot;initiatingMessage&quot; size=&quot;20&quot; pos=&quot;24&quot; show=&quot;&quot; value=&quot;&quot;&gt;
        &lt;field name=&quot;ranap.procedureCode&quot; showname=&quot;procedureCode: id-CommonID (15)&quot; size=&quot;1&quot; pos=&quot;25&quot; show=&quot;15&quot; value=&quot;0f&quot;/&gt;
        &lt;field name=&quot;per.enum_index&quot; showname=&quot;Enumerated Index: 1&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;26&quot; show=&quot;1&quot; value=&quot;40&quot;/&gt;
        &lt;field name=&quot;ranap.criticality&quot; showname=&quot;criticality: ignore (1)&quot; size=&quot;1&quot; pos=&quot;26&quot; show=&quot;1&quot; value=&quot;40&quot;/&gt;
        &lt;field name=&quot;per.open_type_length&quot; showname=&quot;Open Type Length: 16&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;27&quot; show=&quot;16&quot; value=&quot;10&quot;/&gt;
        &lt;field name=&quot;ranap.value&quot; showname=&quot;value&quot; size=&quot;16&quot; pos=&quot;28&quot; show=&quot;&quot; value=&quot;&quot;&gt;
          &lt;field name=&quot;ranap.CommonID&quot; showname=&quot;CommonID&quot; size=&quot;16&quot; pos=&quot;28&quot; show=&quot;&quot; value=&quot;&quot;&gt;
            &lt;field name=&quot;per.extension_bit&quot; showname=&quot;0... .... Extension Bit: False&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;28&quot; show=&quot;0&quot; value=&quot;0&quot; unmask=&quot;&quot; edvalue=&quot;00&quot;/&gt;
            &lt;field name=&quot;per.optional_field_bit&quot; showname=&quot;.0.. .... Optional Field Bit: False (protocolExtensions is NOT present)&quot; hide=&quot;ye
s&quot; size=&quot;1&quot; pos=&quot;28&quot; show=&quot;0&quot; value=&quot;0&quot; unmaskedvalue=&quot;00&quot;/&gt;
            &lt;field name=&quot;per.sequence_of_length&quot; showname=&quot;Sequence-Of Length: 1&quot; hide=&quot;yes&quot; size=&quot;2&quot; pos=&quot;29&quot; show=&quot;1&quot; value=&quot;0001&quot;/&gt;
            &lt;field name=&quot;ranap.protocolIEs&quot; showname=&quot;protocolIEs: 1 item&quot; size=&quot;13&quot; pos=&quot;31&quot; show=&quot;1&quot; value=&quot;001740095022020000000000f0&quot;&gt;
              &lt;field name=&quot;&quot; show=&quot;Item 0: id-PermanentNAS-UE-ID&quot; size=&quot;13&quot; pos=&quot;31&quot; value=&quot;001740095022020000000000f0&quot;&gt;
                &lt;field name=&quot;ranap.ProtocolIE_Field&quot; showname=&quot;ProtocolIE-Field&quot; size=&quot;13&quot; pos=&quot;31&quot; show=&quot;&quot; value=&quot;&quot;&gt;
                  &lt;field name=&quot;ranap.id&quot; showname=&quot;id: id-PermanentNAS-UE-ID (23)&quot; size=&quot;2&quot; pos=&quot;31&quot; show=&quot;23&quot; value=&quot;0017&quot;/&gt;
                  &lt;field name=&quot;per.enum_index&quot; showname=&quot;Enumerated Index: 1&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;33&quot; show=&quot;1&quot; value=&quot;40&quot;/&gt;
                  &lt;field name=&quot;ranap.criticality&quot; showname=&quot;criticality: ignore (1)&quot; size=&quot;1&quot; pos=&quot;33&quot; show=&quot;1&quot; value=&quot;40&quot;/&gt;
                  &lt;field name=&quot;per.open_type_length&quot; showname=&quot;Open Type Length: 9&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;34&quot; show=&quot;9&quot; value=&quot;09&quot;/&gt;
                  &lt;field name=&quot;ranap.value&quot; showname=&quot;value&quot; size=&quot;9&quot; pos=&quot;35&quot; show=&quot;&quot; value=&quot;&quot;&gt;
                    &lt;field name=&quot;per.extension_bit&quot; showname=&quot;0... .... Extension Bit: False&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;35&quot; show=&quot;0&quot; value=&quot;0
&quot; unmaskedvalue=&quot;50&quot;/&gt;
                    &lt;field name=&quot;ranap.PermanentNAS_UE_ID&quot; showname=&quot;PermanentNAS-UE-ID: iMSI (0)&quot; size=&quot;9&quot; pos=&quot;35&quot; show=&quot;0&quot; value=&quot;5022020
000000000f0&quot;&gt;
                      &lt;field name=&quot;per.octet_string_length&quot; showname=&quot;Octet String Length: 8&quot; hide=&quot;yes&quot; size=&quot;1&quot; pos=&quot;35&quot; show=&quot;8&quot; value=&quot;5
0&quot;/&gt;
                      &lt;field name=&quot;ranap.iMSI&quot; showname=&quot;iMSI: 22020000000000f0&quot; size=&quot;8&quot; pos=&quot;36&quot; show=&quot;22:02:00:00:00:00:00:f0&quot; value=&quot;220
20000000000f0&quot;/&gt;
                      &lt;field name=&quot;ranap.imsi_digits&quot; showname=&quot;IMSI digits: 222000000000000&quot; size=&quot;8&quot; pos=&quot;36&quot; show=&quot;222000000000000&quot; value=&quot;22020000000000f0&quot;/&gt;
                    &lt;/field&gt;
                  &lt;/field&gt;
                &lt;/field&gt;
              &lt;/field&gt;
            &lt;/field&gt;
          &lt;/field&gt;
        &lt;/field&gt;
      &lt;/field&gt;
    &lt;/field&gt;
  &lt;/proto&gt;
&lt;/packet&gt;
&lt;/pdml&gt;</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '13, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Oct '13, 05:18</strong> </span></p></div></div><div id="comments-container-25914" class="comments-container"><span id="25952"></span><div id="comment-25952" class="comment"><div id="post-25952-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot!</p></div><div id="comment-25952-info" class="comment-info"><span class="comment-age">(14 Oct '13, 02:20)</span> <span class="comment-user userinfo">Ric79</span></div></div><span id="25954"></span><div id="comment-25954" class="comment"><div id="post-25954-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I have now a frame similar to first one ( <a href="http://speedy.sh/F7txe/mynewpacket.pcap">link text</a> ). It is not mtp3 but bssap.</p><p>Windows wireshark is configured as before (<a href="http://speedy.sh/GQZaH/2013-10-14-120434.png">link text</a>)</p><pre><code>uat:user_dlts:\&quot;User 15 (DLT=162)\&quot;,\&quot;pcap\&quot;,\&quot;0\&quot;,\&quot;\&quot;,\&quot;0\&quot;,\&quot;\&quot; 
uat:user_dlts:\&quot;User 15 (DLT=162)\&quot;,\&quot;mtp3\&quot;,\&quot;12\&quot;,\&quot;\&quot;,\&quot;0\&quot;,\&quot;\&quot;</code></pre><p>and it is able to decode frame (<a href="http://speedy.sh/etDFa/2013-10-14-120536.png">link text</a>)</p><p>With tshark, I do not understand now the right syntax for decoding packet. Could you help me?</p><p>Riccardo</p></div><div id="comment-25954-info" class="comment-info"><span class="comment-age">(14 Oct '13, 03:08)</span> <span class="comment-user userinfo">Ric79</span></div></div></div><div id="comment-tools-25914" class="comment-tools"></div><div class="clear"></div><div id="comment-25914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


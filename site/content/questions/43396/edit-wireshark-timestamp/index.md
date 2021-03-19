+++
type = "question"
title = "edit wireshark timestamp"
description = '''i know wireshark get time stamp for captured packet from system clock  i want to edit this timestamp for specific packets  when i use time shift option in edit menu it changes timestamp for all packets  i need to change time stamp for only one packet  other packet editing tools (for windows OS) allo...'''
date = "2015-06-20T04:56:00Z"
lastmod = "2015-06-21T14:30:00Z"
weight = 43396
keywords = [ "timestamp" ]
aliases = [ "/questions/43396" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [edit wireshark timestamp](/questions/43396/edit-wireshark-timestamp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43396-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i know wireshark get time stamp for captured packet from system clock</p><p>i want to edit this timestamp for specific packets</p><p>when i use time shift option in edit menu it changes timestamp for all packets</p><p>i need to change time stamp for only one packet</p><p>other packet editing tools (for windows OS) allow to edit packet contents not timestamp given by wireshark</p><p>thank you</p></div><div id="question-tags" class="tags-container tags">timestamp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '15, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/583f60448e616e6c6f8408eb6620006a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shady&#39;s gravatar image" /><p>shady<br />
<span class="score" title="11 reputation points">11</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shady has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Jun '15, 05:14</p></div></div><div id="comments-container-43396" class="comments-container"></div><div id="comment-tools-43396" class="comment-tools"></div><div class="clear"></div><div id="comment-43396-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43399"></span>

<div id="answer-container-43399" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43399-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here is one possible solution, but there may be smarter ones.</p><p>Let´s assume the tracefile is called "timetest.pcapng". Open the trace file and note the timestamp of each packet you want to manipulate. Then export the trace as a "k12 text file". Open the new "k12 text file" and manipulate the timestamps you want. Then open the "k12 text file" in wireshark and export it as a pcapng file, e.g. "timeTest2.pcapng". Now you have to reorder the trace. You can do this with the following command:</p><pre><code>reordercap timeTest2.pcapng timetestFinal.pcapng</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '15, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div></div><div id="comments-container-43399" class="comments-container"><span id="43420"></span><div id="comment-43420" class="comment"><div id="post-43420-score" class="comment-score"></div><div class="comment-text"><p>it worked but when i open texe file with wireshark it gives my error message :</p><p>The capture file appears to be damaged or corrupt. (vwr: Invalid data length 2119269 (runs past the end of the record))</p><p>why?</p></div><div id="comment-43420-info" class="comment-info"><span class="comment-age">(21 Jun '15, 14:40)</span> shady</div></div><span id="43422"></span><div id="comment-43422" class="comment"><div id="post-43422-score" class="comment-score"></div><div class="comment-text"><p>hm seems like you changed something more. You can have a look in my manipulated "k12 text file" with this link: <a href="https://crnetworking-my.sharepoint.com/personal/creusch_crnetworks_de/_layouts/15/guestaccess.aspx?guestaccesstoken=9cr0mpAyzD8bZ2plFgs%2fdnQcg6RuRoY%2fpNuRJHicjRQ%3d&amp;docid=0bf081305167e4e158d79a3aef7ab640a">Link to timeTest.txt</a></p><p>As you can see I have changed the time of the second frame. Are you able to open this file without errors?</p></div><div id="comment-43422-info" class="comment-info"><span class="comment-age">(21 Jun '15, 15:22)</span> Christian_R</div></div><span id="43423"></span><div id="comment-43423" class="comment"><div id="post-43423-score" class="comment-score"></div><div class="comment-text"><p>Ok I think I got the fault you didn´t export the file as a "k12 text file". You have to export the file as a "k12 text file" to do this you have to do the following: open the following menu File -&gt; Save as... And as a Filetyp you should select the entry "K12 text file" Then choose a filename and click the save button.</p></div><div id="comment-43423-info" class="comment-info"><span class="comment-age">(21 Jun '15, 15:44)</span> Christian_R</div></div><span id="43424"></span><div id="comment-43424" class="comment"><div id="post-43424-score" class="comment-score"></div><div class="comment-text"><p>i did it thank you 1000000000 times</p><p>to be clear</p><p>choose export specified packets and choose k12 txt before you save then apply mentioned steps this will do the trick ((for time only not date ))</p><p>thank you again</p></div><div id="comment-43424-info" class="comment-info"><span class="comment-age">(21 Jun '15, 15:48)</span> shady</div></div></div><div id="comment-tools-43399" class="comment-tools"></div><div class="clear"></div><div id="comment-43399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43419"></span>

<div id="answer-container-43419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43419-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>One option would be to use a HEX editor that is able to "decode" pcap files to modify the timestamps directly in the pcap file. See the following blog entry of @Jasper and the HEX editor mentioned therein (<a href="http://www.sweetscape.com/010editor/">010 Editor</a> with its PCAP template <a href="http://www.sweetscape.com/010editor/templates/">'PCAPTemplate.bt'</a>).</p><blockquote><p><a href="https://blog.packet-foo.com/2015/04/deep-dive-frame-timestamps/#more-483">https://blog.packet-foo.com/2015/04/deep-dive-frame-timestamps/#more-483</a></p></blockquote><p>Another option would be to use 'special' pcap tools. <a href="https://wireedit.com/">WireEdit</a> seems to get a timestamp modification feature soon (<a href="https://twitter.com/Wirefloss/status/610825578740998145">see Twitter</a>). Besides that tool, you can use <a href="http://www.secdev.org/projects/scapy/">scapy</a> to modifiy the timestamp, however it requires (decent) Python scripting knowledge (see google for examples: <a href="http://lmgtfy.com/?q=scapy+modify+timestamp">scapy modify timestamp</a>).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '15, 14:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-43419" class="comments-container"><span id="43421"></span><div id="comment-43421" class="comment"><div id="post-43421-score" class="comment-score"></div><div class="comment-text"><p>thank you for information i will try 010 editor</p></div><div id="comment-43421-info" class="comment-info"><span class="comment-age">(21 Jun '15, 14:50)</span> shady</div></div><span id="43425"></span><div id="comment-43425" class="comment"><div id="post-43425-score" class="comment-score"></div><div class="comment-text"><p>010 editor gives me wrong timestamps its not clear for me but still</p><p>thank you very much for every thing :))</p></div><div id="comment-43425-info" class="comment-info"><span class="comment-age">(21 Jun '15, 15:50)</span> shady</div></div></div><div id="comment-tools-43419" class="comment-tools"></div><div class="clear"></div><div id="comment-43419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


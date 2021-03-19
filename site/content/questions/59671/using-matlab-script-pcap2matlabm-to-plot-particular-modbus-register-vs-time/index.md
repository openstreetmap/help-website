+++
type = "question"
title = "[closed] Using Matlab script pcap2matlab.m to plot particular Modbus Register vs Time"
description = '''I am using the Matlab script pcap2matlab.m to create a time plot of a Modbus register. (The Matlab script calls TShark).  In Wireshark I can see the parameter I want:  To plot this Modbus register as a function of time I am using pcap2matlab.m. I created a simple script to call pcap2matlab.m for thi...'''
date = "2017-02-24T12:54:00Z"
lastmod = "2017-02-24T12:54:00Z"
weight = 59671
keywords = [ "modbus", "pcap2matlab", "matlab", "pcap2matlab.m" ]
aliases = [ "/questions/59671" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Using Matlab script pcap2matlab.m to plot particular Modbus Register vs Time](/questions/59671/using-matlab-script-pcap2matlabm-to-plot-particular-modbus-register-vs-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59671-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the Matlab script pcap2matlab.m to create a time plot of a Modbus register. (The Matlab script calls TShark).<br />
</p><p>In Wireshark I can see the parameter I want: <img src="https://osqa-ask.wireshark.org/upfiles/modbusTrace_HhXsXF5.jpg" alt="alt text" /></p><p>To plot this Modbus register as a function of time I am using pcap2matlab.m. I created a simple script to call pcap2matlab.m for this purpose. This script is listed below:</p><hr /><p>%pcap2matlab_example2() isRead = true;</p><p>CAPTURE_FILE = 'REL2_test02_onOffHVPW.pcapng'; %% Set up the capturing/reading parameters: dissector = {'modbus.func_code',... 'modbus.request_frame',... 'modbus.byte_cnt',... 'modbus.reg32'};</p><p>capture_filter = 'tcp and src port 502';<br />
read_filter = 'modbus'; %% Capture/read:<br />
if isRead % Read: pcap_result = pcap2matlab(read_filter, dissector, CAPTURE_FILE); else % Capture: pcap_result = pcap2matlab(capture_filter,dissector, 4, 700); end</p><hr /><p>And it works, I get a result for each packet in a Matlab structure array! However, it gives me all the Modbus registers for a given packet combined as a single large decimal, like 5.1205e+247. How can I extract the Modbus register I want from this large decimal (i.e. Register 5523 = 1234.900635 in the image above)?</p></div><div id="question-tags" class="tags-container tags">modbus pcap2matlab matlab pcap2matlab.m</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '17, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/dc183a0a76a78266937363c87d768eaa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmain57&#39;s gravatar image" /><p>bmain57<br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmain57 has no accepted answers">0%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p>closed 27 Feb '17, 07:45</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></br></p></div></div><div id="comments-container-59671" class="comments-container"><span id="59710"></span><div id="comment-59710" class="comment"><div id="post-59710-score" class="comment-score"></div><div class="comment-text"><p>This question is a duplicate of <a href="https://ask.wireshark.org/questions/59670/extract-particular-register-from-series-of-modbus-packets">https://ask.wireshark.org/questions/59670/extract-particular-register-from-series-of-modbus-packets</a> and will be closed.</p></div><div id="comment-59710-info" class="comment-info"><span class="comment-age">(27 Feb '17, 07:45)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-59671" class="comment-tools"></div><div class="clear"></div><div id="comment-59671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by cmaynard 27 Feb '17, 07:45

</div>

</div>

</div>


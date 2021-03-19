+++
type = "question"
title = "Tshark doesn&#x27;t display mbtcp function 4 modbus.data"
description = '''Hi, I&#x27;m completely new to tshark so any help would be much appreviated also quite new to Modbus. I&#x27;m trying extract the raw modbus data from a capture. I&#x27;ve used similar code found in another question Tshark doesn&#x27;t display the longer data fields (mbtcp) but I believe this is a different issue as I&#x27;...'''
date = "2015-07-06T23:07:00Z"
lastmod = "2015-07-12T21:57:00Z"
weight = 43915
keywords = [ "modbus", "mbtcp" ]
aliases = [ "/questions/43915" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark doesn't display mbtcp function 4 modbus.data](/questions/43915/tshark-doesnt-display-mbtcp-function-4-modbusdata)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43915-score" class="post-score" title="current number of votes">0</div><span id="post-43915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm completely new to tshark so any help would be much appreviated also quite new to Modbus.</p><p>I'm trying extract the raw modbus data from a capture. I've used similar code found in another question <a href="https://ask.wireshark.org/questions/28050/tshark-doesnt-display-the-longer-data-fields-mbtcp?">Tshark doesn't display the longer data fields (mbtcp)</a> but I believe this is a different issue as I'm using standard function codes.<br />
</p><p>I have filtered the wireshark data for ip.addr and mbtcp then passed the result through</p><pre><code>tshark -o &quot;opensafety.enable_mbtcp:0&quot; -nr capture.pcapng -Y &quot;mbtcp&quot; -T fields -E header=y -e ip.src -e ip.dst -e mbtcp.unit_id -e modbus.func_code -e modbus.data &gt; tshark_out.txt</code></pre><p>modbus.data only extracts with function code 2 not 4. I have tried the suggestion on the link and included '-o "opensafety.enable_mbtcp:0"' but that doesn't look to sort my issue. Is there anything further someone could suggest that i'm missing?</p><p>Output example:<br />
ip.src ip.dst mbtcp.unit_id modbus.func_code modbus.data<br />
192.168.0.10 192.168.0.20 10 4<br />
192.168.0.20 192.168.0.10 10 4<br />
192.168.0.10 192.168.0.20 10 2<br />
192.168.0.20 192.168.0.10 10 2 00:00:00</p><p>Also I would like to pull out the query start address and less importantly the number of registers to read but I can't find a -e field that will do this. Is it possible?</p><p>Any insight would be greatly recieved as I've been trying to figure this out for a while now. Thanks, Alex</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-modbus" rel="tag" title="see questions tagged &#39;modbus&#39;">modbus</span> <span class="post-tag tag-link-mbtcp" rel="tag" title="see questions tagged &#39;mbtcp&#39;">mbtcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '15, 23:07</strong></p><img src="https://secure.gravatar.com/avatar/8b3cb5d834ae2a0ad0043fe866c15dbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="agraybill&#39;s gravatar image" /><p><span>agraybill</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="agraybill has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-43915" class="comments-container"></div><div id="comment-tools-43915" class="comment-tools"></div><div class="clear"></div><div id="comment-43915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43916"></span>

<div id="answer-container-43916" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43916-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43916-score" class="post-score" title="current number of votes">0</div><span id="post-43916-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Function code 4 is "read input registers", where the request payload (the first frame in your text output) consists of the starting register offset (16 bits) and the count of registers to read (also 16 bit). These two files have field identifiers of <code>modbus.reference_num</code> and <code>modbus.word_cnt</code> respectively.</p><p>The response (the 2nd frame in your text) will have an 8 bit byte count (field identifier <code>modbus.byte_cnt</code>) followed by the register data. The register data is decoded according to the dissector preference "Holding/Input Register Format", which defaults to unsigned 16 bit integers, the field identifier for this data is <code>modbus.register.uint16</code>. I'm not certain how multiple registers will be displayed with a single <code>-e modbus.register.uint16</code> argument, I'll test later at work.</p><p>The <code>modbus.data</code> field identifier is only used to output "raw" values where there is an issue with the data (incorrect length) or a 32 bit format is specified in the preferences but there aren't 4 bytes of data, or an unknown function code.</p><p>You can easily determine field identifiers yourself by clicking on a field in the packet details tree and checking the status bar where the field identifier is shown in parentheses.</p><p>If you can share a capture with the required data (in a public spot, e.g. <a href="http://cloudshark.org">Cloudshark</a>, Google Drive etc.), then that will help to analyse your issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '15, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></br></p></div></div><div id="comments-container-43916" class="comments-container"><span id="44082"></span><div id="comment-44082" class="comment"><div id="post-44082-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick response.</p><p>I have uploaded a capture to <a href="https://drive.google.com/file/d/0B7OjePa-tOLSaWg1NFJ6b01kaHM/view?usp=sharing">Google Drive</a></p><p>I should have given some more background info. I am currently having an issue where the analogue data is spiking extreme high/extreme low/set constant value. At the moment I am unsure where the issue is so I am wanting to analyse the data to make sure that the requests/responses are not getting mixed up or that the field device isn't corrupting the data etc. These 'corruptions' are happening irregularly so I want to be able to analyse a large amount of data and see what the messaging is doing around the 'corruption'</p><p>The analogue field data is either 32-bit float LH or 32-bit integer HL which I believe I have to extract using <code>modbus.data</code>. I was going to translate the extract using Excel but if you have another recommendation I'm all ears.</p><p>Cheers, Alex</p></div><div id="comment-44082-info" class="comment-info"><span class="comment-age">(12 Jul '15, 21:57)</span> <span class="comment-user userinfo">agraybill</span></div></div></div><div id="comment-tools-43916" class="comment-tools"></div><div class="clear"></div><div id="comment-43916-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


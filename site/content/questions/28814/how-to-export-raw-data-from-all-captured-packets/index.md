+++
type = "question"
title = "How to export raw data from all captured packets?"
description = '''Hi, I have a lot of UDP packets captured where I want to save the raw data (bytes) of each packet in a separate file. The way I&#x27;m doing it currently is that I select the packet, select the data bytes and do Strg+H (Export selected packet bytes). But since there are a lot of packets this is of course...'''
date = "2014-01-12T04:40:00Z"
lastmod = "2014-01-12T05:55:00Z"
weight = 28814
keywords = [ "raw", "bytes", "export" ]
aliases = [ "/questions/28814" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to export raw data from all captured packets?](/questions/28814/how-to-export-raw-data-from-all-captured-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28814-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a lot of UDP packets captured where I want to save the raw data (bytes) of each packet in a separate file.</p><p>The way I'm doing it currently is that I select the packet, select the data bytes and do Strg+H (Export selected packet bytes). But since there are a lot of packets this is of course not a good solution for me.</p><p>So is it possible to just export the raw data in separate files from all captured (or filtered) packets at once?</p><p>If possible I would also like to give the files names that give further indication how the traffic happened, like [packet_number]<em>[src_port]</em>[dest_port].bin</p></div><div id="question-tags" class="tags-container tags">raw bytes export</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '14, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/7a10a42836e761c7d644ecfe249b8d70?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="michael825&#39;s gravatar image" /><p>michael825<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="michael825 has no accepted answers">0%</span></p></div></div><div id="comments-container-28814" class="comments-container"></div><div id="comment-tools-28814" class="comment-tools"></div><div class="clear"></div><div id="comment-28814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28815"></span>

<div id="answer-container-28815" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28815-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In case you are interested I could offer you a special build of <a href="http://www.tracewrangler.com">TraceWrangler</a> that can do this on Windows. It took me 20 minutes to hack that sort of processing into the program by using a temporary button on the main form, so this is neither pretty nor will it stay that way for the next official version. And if it crashes for you I probably won't have time to fix anything in the next couple of days.</p><p>I did not test it much, but it seems to work, even on a list of traces (I used a couple of DHCPv4 packets in 4 single PCAPng traces, 1 frame per file). For that I changed your output file naming scheme for the exported payloads to [filenumber]<em>[packet_number]</em>[src_port]-[dest_port].bin, because otherwise outputs are overwritten every once in a while. Send me an email to [email protected] if you're interested.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '14, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28815" class="comments-container"><span id="28816"></span><div id="comment-28816" class="comment"><div id="post-28816-score" class="comment-score"></div><div class="comment-text"><p>If there isn't any other way to do this then of course I would be interested (I sent the email already).</p><p>Though if the basic functionality of exporting the data in files is there (and the packets would just be given numerical names) then I could help myself with filtering out the packets before exporting them.</p><p>The only question is if there is such a functionality (and if not why, I mean I don't think this would be considered an exotic feature...)?</p></div><div id="comment-28816-info" class="comment-info"><span class="comment-age">(12 Jan '14, 06:57)</span> michael825</div></div><span id="28817"></span><div id="comment-28817" class="comment"><div id="post-28817-score" class="comment-score"></div><div class="comment-text"><p>most people probably help themselves with tshark scripts or the export to text file functionality, and then write custom scripts to process them further. At least that's my guess.</p></div><div id="comment-28817-info" class="comment-info"><span class="comment-age">(12 Jan '14, 07:19)</span> Jasper ♦♦</div></div></div><div id="comment-tools-28815" class="comment-tools"></div><div class="clear"></div><div id="comment-28815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


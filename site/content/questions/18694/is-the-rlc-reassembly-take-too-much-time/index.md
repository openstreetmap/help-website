+++
type = "question"
title = "is the rlc reassembly take too much time?"
description = '''When I open a .pcap on wireshark1.8.5. Is take very long time. about 15 minute, size of the .pcap is 90 MB. why it took so long time?  In the *.pcap, there are many rlc rrc message.is the rlc reassembly step take too much time ? Thanks!'''
date = "2013-02-17T19:52:00Z"
lastmod = "2013-02-17T19:52:00Z"
weight = 18694
keywords = [ "reassembly", "rrc", "rlc", "time" ]
aliases = [ "/questions/18694" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [is the rlc reassembly take too much time?](/questions/18694/is-the-rlc-reassembly-take-too-much-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18694-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I open a <em>.pcap on wireshark1.8.5. Is take very long time. about 15 minute, size of the</em> .pcap is 90 MB.</p><p>why it took so long time?</p><p>In the *.pcap, there are many rlc rrc message.is the rlc reassembly step take too much time ?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">reassembly rrc rlc time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '13, 19:52</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p>smilezuzu<br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-18694" class="comments-container"><span id="18697"></span><div id="comment-18697" class="comment"><div id="post-18697-score" class="comment-score"></div><div class="comment-text"><p>Possibly, if you could raise a bug report including the trace file that might help to find out if anything can be done to speed it up or you could run a profiler tool.</p></div><div id="comment-18697-info" class="comment-info"><span class="comment-age">(17 Feb '13, 22:22)</span> Anders ♦</div></div><span id="18698"></span><div id="comment-18698" class="comment"><div id="post-18698-score" class="comment-score"></div><div class="comment-text"><p>the *.pcap file is too big to upload. and there is no bug report, just took too much time to decode.</p></div><div id="comment-18698-info" class="comment-info"><span class="comment-age">(17 Feb '13, 23:40)</span> smilezuzu</div></div><span id="18699"></span><div id="comment-18699" class="comment"><div id="post-18699-score" class="comment-score"></div><div class="comment-text"><p>Still, if you open a bug at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a> I think you can add the file therwe.</p></div><div id="comment-18699-info" class="comment-info"><span class="comment-age">(18 Feb '13, 00:22)</span> Anders ♦</div></div><span id="18700"></span><div id="comment-18700" class="comment"><div id="post-18700-score" class="comment-score"></div><div class="comment-text"><p>could you help me? Another question: 1,How did the rlc reassemble the code from mac in wireshark? you should tell me the main step of reassemble in wireshark.</p><p>2,Is the wireshark malloc memory for each rlc SDU? because when the wireshark decode a big *.pcap,it will occupy a big memory.</p><p>Thanks!</p></div><div id="comment-18700-info" class="comment-info"><span class="comment-age">(18 Feb '13, 00:31)</span> smilezuzu</div></div><span id="18701"></span><div id="comment-18701" class="comment"><div id="post-18701-score" class="comment-score"></div><div class="comment-text"><p>added, if the wireshark reassemble the code from mac like this step: 1,decode each rlc code and malloc new memory for each rlc SDU. 2,when user click the frame .wireshark will find the rlc SDU's which have the same logical channel id. and then reassemble those ,transport to up level. 3,so for each rlc decode,it need to search the memory which malloced by rlc. if the memory is big, then the time used to decode is long.</p></div><div id="comment-18701-info" class="comment-info"><span class="comment-age">(18 Feb '13, 00:46)</span> smilezuzu</div></div></div><div id="comment-tools-18694" class="comment-tools"></div><div class="clear"></div><div id="comment-18694-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


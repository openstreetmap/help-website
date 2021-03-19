+++
type = "question"
title = "Multi-file search"
description = '''Is there a mechanism where multiple files can be searched for a particular parameter? When capturing large amounts of data or there is an intermittent issue and you are collecting the capture off in a ring buffer. The problem is when the event, lets say a SIP call overlaps 20 files, pulling all the ...'''
date = "2011-08-12T13:31:00Z"
lastmod = "2011-08-12T16:58:00Z"
weight = 5691
keywords = [ "sip", "rtp", "tshark", "analysis", "script" ]
aliases = [ "/questions/5691" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multi-file search](/questions/5691/multi-file-search)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5691-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5691-score" class="post-score" title="current number of votes">0</div><span id="post-5691-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a mechanism where multiple files can be searched for a particular parameter?</p><p>When capturing large amounts of data or there is an intermittent issue and you are collecting the capture off in a ring buffer. The problem is when the event, lets say a SIP call overlaps 20 files, pulling all the SIP and RTP out of the various files is very time consuming.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-script" rel="tag" title="see questions tagged &#39;script&#39;">script</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '11, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/68628b64cd0e92525d4ed3c53b3af4ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dpackboy&#39;s gravatar image" /><p><span>dpackboy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dpackboy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Aug '11, 17:59</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5691" class="comments-container"></div><div id="comment-tools-5691" class="comment-tools"></div><div class="clear"></div><div id="comment-5691-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5697"></span>

<div id="answer-container-5697" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5697-score" class="post-score" title="current number of votes">2</div><span id="post-5697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd use a batch file and tshark to do this. You can use the parameters "-r" to read a file, "-R" to apply any display filter you'd manually use, and "-w" to write the resulting frames back to a new trace, for example:</p><p><code>tshark -r "sample.pcap" -R "ftp or ftp-data" -w "just-ftp.pcap"</code></p><p>That way my resulting trace file named "just-ftp.pcap" will only have packets that contain FTP or FTP data flows. You can run that kind of command on any number of files in a loop or by single commands batched together.</p><p>Afterwards you might use mergecap to merge your resulting fragments together into one single pcap file.</p><p>tshark and mergecap are command line tools installed together with Wireshark, so it is most likely you already have them on your computer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '11, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-5697" class="comments-container"></div><div id="comment-tools-5697" class="comment-tools"></div><div class="clear"></div><div id="comment-5697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


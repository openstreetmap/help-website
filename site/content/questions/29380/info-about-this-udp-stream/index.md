+++
type = "question"
title = "info about this UDP stream"
description = '''I took a sample malware to analyze with a wireshark. This malware is a Zeus Bot. So I was taking a look at this UDP stream, why it didn&#x27;t give me some more clear information? Here you can download a PCAP file '''
date = "2014-02-02T05:04:00Z"
lastmod = "2014-02-02T05:14:00Z"
weight = 29380
keywords = [ "malware", "analysis", "wireshark" ]
aliases = [ "/questions/29380" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [info about this UDP stream](/questions/29380/info-about-this-udp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29380-score" class="post-score" title="current number of votes">0</div><span id="post-29380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I took a sample malware to analyze with a wireshark. This malware is a Zeus Bot. So I was taking a look at this UDP stream, why it didn't give me some more clear information? Here you can download a <a href="http://www.sendspace.com/file/1uo8r4">PCAP</a> file</p><p><img src="https://osqa-ask.wireshark.org/upfiles/1_1.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malware" rel="tag" title="see questions tagged &#39;malware&#39;">malware</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '14, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/bd23f18ea1f2b5981020717fb5be41cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Espen&#39;s gravatar image" /><p><span>Espen</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Espen has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Feb '14, 05:05</strong> </span></p></div></div><div id="comments-container-29380" class="comments-container"></div><div id="comment-tools-29380" class="comment-tools"></div><div class="clear"></div><div id="comment-29380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29381"></span>

<div id="answer-container-29381" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29381-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29381-score" class="post-score" title="current number of votes">1</div><span id="post-29381-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Espen has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thats because those UDP packets just do not contain human readable ASCII information. It may be a binary format, or just be packed, encrypted, or both, so it has a quite high entropy and cannot be read just as a normal text. You could track down the Zeus guys and complain to them that they should do their stuff in an easily readable way, but I doubt they'll listen (even if you could find them) - they do not WANT you to find out what they're doing.</p><p>BTW, I'm not entirely sure if those UDP packets are the Zeus stuff after all by the way. Yes, there is Zeus communication in your trace, but it communicates via TCP starting in frame 347, which you can (mostly) read by doing "Follow TCP stream". The UDP stuff you mention could be something else entirely and not be related to Zeus.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '14, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-29381" class="comments-container"></div><div id="comment-tools-29381" class="comment-tools"></div><div class="clear"></div><div id="comment-29381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Reassembling/Merge failure"
description = '''Hi, I received a capture from a client for analyze. Unfortunately if i can open the individual splitted files in Wireshark (tried with 1.10.6 x64 &amp;amp; x32), I cannot merge the files. I tried to do it from Wireshark itself and using mergecap but each time I receive the same error : D:&#92;tmp&#92;capture&#92;da...'''
date = "2014-03-21T00:47:00Z"
lastmod = "2014-03-21T07:17:00Z"
weight = 31044
keywords = [ "merge", "mergecap", "split" ]
aliases = [ "/questions/31044" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Reassembling/Merge failure](/questions/31044/reassemblingmerge-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31044-score" class="post-score" title="current number of votes">0</div><span id="post-31044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I received a capture from a client for analyze. Unfortunately if i can open the individual splitted files in Wireshark (tried with 1.10.6 x64 &amp; x32), I cannot merge the files. I tried to do it from Wireshark itself and using mergecap but each time I receive the same error :</p><pre><code>D:\tmp\capture\data&gt;ls
shark10380_00001_20140320094921  shark10380_00002_20140320095016

D:\tmp\capture\data&gt;mergecap -v -w ..\merged.pcapng shark*.*
mergecap: shark10380_00001_20140320094921 is type Wireshark/... - pcapng.
mergecap: shark10380_00002_20140320095016 is type Wireshark/... - pcapng.
mergecap: selected frame_type Ethernet (ether)
Record: 1
mergecap: Error writing to outfile: Error -23</code></pre><p>Of course I have space left on the disk and the directories are writable. I have no idea on what the problem is. I did exactly the same for another analysis received also yesterday from the same client that I could merge successfully.</p><p>Thanks if someone can help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-mergecap" rel="tag" title="see questions tagged &#39;mergecap&#39;">mergecap</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '14, 00:47</strong></p><img src="https://secure.gravatar.com/avatar/e15d589760570212208397913e06963b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="McFoggy&#39;s gravatar image" /><p><span>McFoggy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="McFoggy has no accepted answers">0%</span></p></div></div><div id="comments-container-31044" class="comments-container"></div><div id="comment-tools-31044" class="comment-tools"></div><div class="clear"></div><div id="comment-31044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31045"></span>

<div id="answer-container-31045" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31045-score" class="post-score" title="current number of votes">1</div><span id="post-31045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="McFoggy has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Can you check if there are more than one interface captured in the files? Mergecap does not work with those kind of files, it can only merge files captured on a single interface at this time. It is a known bug.</p><p>Easiest way to check is to open the Summary in the Statistics menu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '14, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31045" class="comments-container"><span id="31046"></span><div id="comment-31046" class="comment"><div id="post-31046-score" class="comment-score"></div><div class="comment-text"><p>You got it right, there are 4 interfaces on this capture while the one that worked previously had only one interface captured. Thanks a lot.</p></div><div id="comment-31046-info" class="comment-info"><span class="comment-age">(21 Mar '14, 05:22)</span> <span class="comment-user userinfo">McFoggy</span></div></div><span id="31049"></span><div id="comment-31049" class="comment"><div id="post-31049-score" class="comment-score"></div><div class="comment-text"><p>We should add a error code string for that, as "-23" isn't too helpful. ;)</p></div><div id="comment-31049-info" class="comment-info"><span class="comment-age">(21 Mar '14, 07:09)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31050"></span><div id="comment-31050" class="comment"><div id="post-31050-score" class="comment-score"></div><div class="comment-text"><p>Actually forget that - it would be almost as much work as just fixing it to handle multiple interfaces. (it's bug 8795, BTW)</p></div><div id="comment-31050-info" class="comment-info"><span class="comment-age">(21 Mar '14, 07:17)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-31045" class="comment-tools"></div><div class="clear"></div><div id="comment-31045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


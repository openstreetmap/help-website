+++
type = "question"
title = "first run - no libwiretap.so.0"
description = '''Hi, I&#x27;ve just build wireshark on SUSE 11.3. There were no problems with compilation and installation, but when I try to run it, there is an error &quot;wireshark: error while loading shared libraries: libwiretap.so.0: cannot open shared object file: No such file or directory&quot;. This library is in /usr/loc...'''
date = "2011-01-16T14:36:00Z"
lastmod = "2014-09-03T01:57:00Z"
weight = 1766
keywords = [ "install" ]
aliases = [ "/questions/1766" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [first run - no libwiretap.so.0](/questions/1766/first-run-no-libwiretapso0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1766-score" class="post-score" title="current number of votes">0</div><span id="post-1766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I've just build wireshark on SUSE 11.3. There were no problems with compilation and installation, but when I try to run it, there is an error "wireshark: error while loading shared libraries: libwiretap.so.0: cannot open shared object file: No such file or directory". This library is in /usr/local/lib but I don't know what to do to run wireshark. Thanks for your help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/d40575b8aff29a33ad4e3fb1ac18e220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomeks1972&#39;s gravatar image" /><p><span>tomeks1972</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomeks1972 has no accepted answers">0%</span></p></div></div><div id="comments-container-1766" class="comments-container"></div><div id="comment-tools-1766" class="comment-tools"></div><div class="clear"></div><div id="comment-1766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1775"></span>

<div id="answer-container-1775" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1775-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1775-score" class="post-score" title="current number of votes">1</div><span id="post-1775-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you tell configure where it would be installed? Check your configure log.</p><p>Otherwise try setting LD_LIBRARY_PATH before launching Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '11, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1775" class="comments-container"></div><div id="comment-tools-1775" class="comment-tools"></div><div class="clear"></div><div id="comment-1775-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1776"></span>

<div id="answer-container-1776" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1776-score" class="post-score" title="current number of votes">0</div><span id="post-1776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you Jaap I solved my problem. In Suse, there was not a such variable. All I had to do was to create a file 'profile.local' in '/etc' with a line inside 'export LD_LIBRARY_PATH=/usr/local/lib'. After reboot everything works fine. See you and good luck.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '11, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/d40575b8aff29a33ad4e3fb1ac18e220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomeks1972&#39;s gravatar image" /><p><span>tomeks1972</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomeks1972 has no accepted answers">0%</span></p></div></div><div id="comments-container-1776" class="comments-container"></div><div id="comment-tools-1776" class="comment-tools"></div><div class="clear"></div><div id="comment-1776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35949"></span>

<div id="answer-container-35949" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35949-score" class="post-score" title="current number of votes">0</div><span id="post-35949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Run 'ldconfig' command(or similar command), Issue should be solved. I had same issue on Ubuntu 14.04, ldconfig helped!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '14, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/46521255c9360a018c61fe9f828b7e62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharan&#39;s gravatar image" /><p><span>Sharan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Sep '14, 01:58</strong> </span></p></div></div><div id="comments-container-35949" class="comments-container"></div><div id="comment-tools-35949" class="comment-tools"></div><div class="clear"></div><div id="comment-35949-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Can&#x27;t install to 32-bit Win 7 machine"
description = '''I uninstalled my previous version (1.6.6) and am attempting to install the latest from the website. On many of the installation files I get an &quot;unable to write to&quot; and then file name error message. All I can do is retry, abort or ignore. If I ignore, installation doesn&#x27;t complete.'''
date = "2013-09-05T16:21:00Z"
lastmod = "2013-09-09T09:07:00Z"
weight = 24399
keywords = [ "installation" ]
aliases = [ "/questions/24399" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can't install to 32-bit Win 7 machine](/questions/24399/cant-install-to-32-bit-win-7-machine)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24399-score" class="post-score" title="current number of votes">0</div><span id="post-24399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I uninstalled my previous version (1.6.6) and am attempting to install the latest from the website.</p><p>On many of the installation files I get an "unable to write to" and then file name error message. All I can do is retry, abort or ignore. If I ignore, installation doesn't complete.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Sep '13, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/042575eed8fec7ab5cf41215b233aab0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="greekgeek82&#39;s gravatar image" /><p><span>greekgeek82</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="greekgeek82 has no accepted answers">0%</span></p></div></div><div id="comments-container-24399" class="comments-container"></div><div id="comment-tools-24399" class="comment-tools"></div><div class="clear"></div><div id="comment-24399-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24485"></span>

<div id="answer-container-24485" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24485-score" class="post-score" title="current number of votes">0</div><span id="post-24485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>On many of the installation files I get an <strong>"unable to write to"</strong> and then file name error message. All I can do is retry, abort or ignore. If I ignore, installation doesn't complete.</p></blockquote><p>I see these (possible) reasons</p><ol><li>You are not running the installer as Administrator (or with equivalent privileges)</li><li>There is a Wireshark/tshark/dumpcap instance still running in the background and thus the OS prevents the installer from overwriting open files (check with: Task Manager)</li><li>The installer file got corrupted during the download (check with: MD5/SHA1 hash from the wireshark download page)</li><li>Some security software on your system (AV, IDS, Endpoint Security, etc.) believes that parts of the installer are malware and thus prevents the process from writing to disk (check the logs of your security software).</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '13, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24485" class="comments-container"></div><div id="comment-tools-24485" class="comment-tools"></div><div class="clear"></div><div id="comment-24485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


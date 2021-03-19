+++
type = "question"
title = "Debian package installation breaks all docker images and most of the scripts in the world"
description = '''When installing tshark on ubuntu 14.04 with command &quot;sudo apt-get install -y tshark&quot; installation goes fine until there is a question  &quot;Should non-superusers be able to capture packets?&quot; even though -y was specified on apt-get install, and hangs the whole installation process. So in brief, all the d...'''
date = "2017-01-15T22:34:00Z"
lastmod = "2017-01-16T03:44:00Z"
weight = 58798
keywords = [ "broken", "installation", "debian" ]
aliases = [ "/questions/58798" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Debian package installation breaks all docker images and most of the scripts in the world](/questions/58798/debian-package-installation-breaks-all-docker-images-and-most-of-the-scripts-in-the-world)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58798-score" class="post-score" title="current number of votes">0</div><span id="post-58798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When installing tshark on ubuntu 14.04 with command "sudo apt-get install -y tshark" installation goes fine until there is a question "Should non-superusers be able to capture packets?" even though -y was specified on apt-get install, and hangs the whole installation process.</p><p>So in brief, all the docker installations and most of the script installations containing wireshark will will now break.</p><p>Another way of doing this would be to ask "Allow only super user to capture packets?" and respect the -y on command line</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broken" rel="tag" title="see questions tagged &#39;broken&#39;">broken</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-debian" rel="tag" title="see questions tagged &#39;debian&#39;">debian</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jan '17, 22:34</strong></p><img src="https://secure.gravatar.com/avatar/54912db5f06bb1a4feac002d7611a20b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaakko%20paakkonen&#39;s gravatar image" /><p><span>jaakko paakk...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaakko paakkonen has no accepted answers">0%</span></p></div></div><div id="comments-container-58798" class="comments-container"></div><div id="comment-tools-58798" class="comment-tools"></div><div class="clear"></div><div id="comment-58798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58805"></span>

<div id="answer-container-58805" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58805-score" class="post-score" title="current number of votes">1</div><span id="post-58805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The person to handle a distribution specific package issue would be the maintainer for that package. See <a href="http://packages.ubuntu.com/trusty/net/tshark">here</a> for the page for that package.</p><p>In short, this is not directly an issue for the Wireshark project.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jan '17, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58805" class="comments-container"></div><div id="comment-tools-58805" class="comment-tools"></div><div class="clear"></div><div id="comment-58805-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


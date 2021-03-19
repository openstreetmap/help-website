+++
type = "question"
title = "invalid key format wireshark 1.8.2"
description = '''I can&#x27;t input my WPA2 key, It keeps saying &quot;invalid key format&quot; , is this a bug and how can I solve the problem? Thanks'''
date = "2012-08-28T22:18:00Z"
lastmod = "2013-03-16T05:00:00Z"
weight = 13951
keywords = [ "bugs", "wireshark" ]
aliases = [ "/questions/13951" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [invalid key format wireshark 1.8.2](/questions/13951/invalid-key-format-wireshark-182)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13951-score" class="post-score" title="current number of votes">0</div><span id="post-13951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can't input my WPA2 key, It keeps saying "invalid key format" , is this a bug and how can I solve the problem?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bugs" rel="tag" title="see questions tagged &#39;bugs&#39;">bugs</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '12, 22:18</strong></p><img src="https://secure.gravatar.com/avatar/fafa8ddd40f29a792c32412cd0737ad4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mierdix&#39;s gravatar image" /><p><span>mierdix</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mierdix has no accepted answers">0%</span></p></div></div><div id="comments-container-13951" class="comments-container"></div><div id="comment-tools-13951" class="comment-tools"></div><div class="clear"></div><div id="comment-13951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13957"></span>

<div id="answer-container-13957" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13957-score" class="post-score" title="current number of votes">2</div><span id="post-13957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this was a bug. I checked in a fix in <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=44694">r44694</a>, which will be scheduled to be backported to the 1.8 branch. For now, if you are running Windows, you can test with any <a href="http://www.wireshark.org/download/automated/">automated build</a> version 44694 or later. If the installer isn't there yet, wait a while until the <a href="http://buildbot.wireshark.org/trunk/waterfall">buildbots</a> have finished creating them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '12, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-13957" class="comments-container"><span id="19544"></span><div id="comment-19544" class="comment"><div id="post-19544-score" class="comment-score"></div><div class="comment-text"><p>when is it going to be fixed?</p></div><div id="comment-19544-info" class="comment-info"><span class="comment-age">(15 Mar '13, 14:02)</span> <span class="comment-user userinfo">trogper</span></div></div><span id="19547"></span><div id="comment-19547" class="comment"><div id="post-19547-score" class="comment-score"></div><div class="comment-text"><p>It was already backported to 1.8.4. Although it's missing from the <a href="http://wiki.wireshark.org/Development/Trunk-1.8">Past 1.8 Releases</a> wikipage, it's in the subversion log <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.8/epan/crypt/airpdcap.c?r1=43119&amp;r2=45127">r45127</a>.</p></div><div id="comment-19547-info" class="comment-info"><span class="comment-age">(15 Mar '13, 14:55)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="19548"></span><div id="comment-19548" class="comment"><div id="post-19548-score" class="comment-score"></div><div class="comment-text"><p>i'm on Ubuntu, installed wireshark throug aptitude and i have just 1.8.2. Who compiles wireshark for Ubuntu?</p></div><div id="comment-19548-info" class="comment-info"><span class="comment-age">(15 Mar '13, 15:37)</span> <span class="comment-user userinfo">trogper</span></div></div><span id="19555"></span><div id="comment-19555" class="comment"><div id="post-19555-score" class="comment-score"></div><div class="comment-text"><p>Checkout the <a href="https://launchpad.net/~dreibh/+archive/ppa">PPA for Thomas Dreibholz</a> for instance.</p></div><div id="comment-19555-info" class="comment-info"><span class="comment-age">(16 Mar '13, 05:00)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-13957" class="comment-tools"></div><div class="clear"></div><div id="comment-13957-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Best way to package our own deployment with recommended decode settings?"
description = '''Hi all -  I&#x27;m trying to work out what the best way is to preconfigure a whole bunch settings for a Wireshark distribution? In particular, I&#x27;ve got a MATE file I&#x27;d like to include and have preset, and I&#x27;ve got 400 ports that I&#x27;ve currently added to the decode_as_entries file, then I&#x27;ve got a few bits...'''
date = "2016-06-28T19:28:00Z"
lastmod = "2016-06-29T23:45:00Z"
weight = 53704
keywords = [ "configuration", "build", "deploy" ]
aliases = [ "/questions/53704" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Best way to package our own deployment with recommended decode settings?](/questions/53704/best-way-to-package-our-own-deployment-with-recommended-decode-settings)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53704-score" class="post-score" title="current number of votes">0</div><span id="post-53704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all - I'm trying to work out what the best way is to preconfigure a whole bunch settings for a Wireshark distribution? In particular, I've got a MATE file I'd like to include and have preset, and I've got 400 ports that I've currently added to the decode_as_entries file, then I've got a few bits I would like to preconfigure for some example filter expressions and deploy that as a standard set of config options when someone is installing for the first time.</p><p>What's the best way to define this and deploy them</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-configuration" rel="tag" title="see questions tagged &#39;configuration&#39;">configuration</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-deploy" rel="tag" title="see questions tagged &#39;deploy&#39;">deploy</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '16, 19:28</strong></p><img src="https://secure.gravatar.com/avatar/c4a59238ef906285e110fa429a9a94b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott%20Harman&#39;s gravatar image" /><p><span>Scott Harman</span><br />
<span class="score" title="46 reputation points">46</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott Harman has one accepted answer">50%</span></p></div></div><div id="comments-container-53704" class="comments-container"></div><div id="comment-tools-53704" class="comment-tools"></div><div class="clear"></div><div id="comment-53704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="53724"></span>

<div id="answer-container-53724" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53724-score" class="post-score" title="current number of votes">1</div><span id="post-53724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Scott Harman has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd look at pushing the files into the "Global configuration" area. From your comments on Anders' answer it sounds like you're on Windows so this is probably something like C:\Program Files\Wireshark (check Help-&gt;About-&gt;Folders).</p><p>I used to do something like this for my (Linux and Solaris) installs: I put a shell of a preferences file (with only the settings I wanted to override) in /usr/local/wireshark/ (or wherever it was). These files are read before the personal configuration files so they give you a reasonable method to override Wireshark's defaults (while allowing users to change their preferences too).</p><p>Just note that I've never actually tried it on Windows but it <em>should</em> work. Another question is if we read all the files you need from this global configuration area. Preferences should be fine but I'm less sure about decode-as entries.</p><p>(I realize I'm not really answering the question about how to actually get the files there.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '16, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-53724" class="comments-container"><span id="53743"></span><div id="comment-53743" class="comment"><div id="post-53743-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@JeffMorriss</span> - I'll give that a shot - I should be able to manually copy the files to staging then edit the nsis to deploy it - after testing it's had the desired effect of course ;) Cheers</p></div><div id="comment-53743-info" class="comment-info"><span class="comment-age">(29 Jun '16, 23:45)</span> <span class="comment-user userinfo">Scott Harman</span></div></div></div><div id="comment-tools-53724" class="comment-tools"></div><div class="clear"></div><div id="comment-53724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53705"></span>

<div id="answer-container-53705" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53705-score" class="post-score" title="current number of votes">1</div><span id="post-53705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd look at copying the preferences from your reference installation to your users.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '16, 22:28</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-53705" class="comments-container"><span id="53706"></span><div id="comment-53706" class="comment"><div id="post-53706-score" class="comment-score"></div><div class="comment-text"><p>Thanks <span>@Anders</span> - yeah, that's the next best option if there's no way to build it into the NSIS installer</p></div><div id="comment-53706-info" class="comment-info"><span class="comment-age">(28 Jun '16, 22:46)</span> <span class="comment-user userinfo">Scott Harman</span></div></div><span id="53711"></span><div id="comment-53711" class="comment"><div id="post-53711-score" class="comment-score"></div><div class="comment-text"><p>Build it into the NSIS installer then :)</p></div><div id="comment-53711-info" class="comment-info"><span class="comment-age">(29 Jun '16, 01:57)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-53705" class="comment-tools"></div><div class="clear"></div><div id="comment-53705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


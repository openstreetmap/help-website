+++
type = "question"
title = "Editing Makefiles to add a plugin in linux"
description = '''I&#x27;ve created a plugin using windows and it builds and runs correctly. I&#x27;m trying to get the plugin to build on CENTOS6 using Wireshark 1.10.5 and I&#x27;m having some issues with the Makefiles. The downloaded source builds fine. The issue starts once I add the plugin. After editing the root, plugins, and...'''
date = "2014-03-06T16:38:00Z"
lastmod = "2014-03-10T16:56:00Z"
weight = 30511
keywords = [ "linux", "makefile", "build", "plugin" ]
aliases = [ "/questions/30511" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Editing Makefiles to add a plugin in linux](/questions/30511/editing-makefiles-to-add-a-plugin-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30511-score" class="post-score" title="current number of votes">0</div><span id="post-30511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've created a plugin using windows and it builds and runs correctly. I'm trying to get the plugin to build on CENTOS6 using Wireshark 1.10.5 and I'm having some issues with the Makefiles. The downloaded source builds fine. The issue starts once I add the plugin. After editing the root, plugins, and my plugin directory Makefiles I keep getting the below error.<br />
</p><p>It seems like all of the google hits for this issue seems to point to bin_PROGRAMS not being defined correctly.<br />
The steps I have taken to add my plugin is edit the root Makefile.am by adding the following to plugin_ldadd</p><pre><code>-dlopen plugins/gar/gar_v1.0.0.la</code></pre><p>in configure.ac I added the following to AC_OUTPUT</p><pre><code>plugins/gar/Makefile</code></pre><p>In plugins/Makefile.am the following was added to SUBDIRS</p><pre><code>gar</code></pre><p>Searching on google for the message hasn't given me much help. What types of things should I be checking to troubleshoot this sort of error?</p><pre><code>plugins/gar/Makefile.am:33: variable `gar_v1.0.0_la_SOURCES&#39; is defined but no program or
plugins/gar/Makefile.am:33: library has `gar_v1.0.0_la&#39; as canonical name (possible typo)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-makefile" rel="tag" title="see questions tagged &#39;makefile&#39;">makefile</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-plugin" rel="tag" title="see questions tagged &#39;plugin&#39;">plugin</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '14, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></br></p></div></div><div id="comments-container-30511" class="comments-container"></div><div id="comment-tools-30511" class="comment-tools"></div><div class="clear"></div><div id="comment-30511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30668"></span>

<div id="answer-container-30668" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30668-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30668-score" class="post-score" title="current number of votes">0</div><span id="post-30668-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tlann has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The plugin was originally created using WS 1.8 and the makefiles were older. After following the new wireshark docs it now builds correctly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '14, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p><span>tlann</span><br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span></p></div></div><div id="comments-container-30668" class="comments-container"></div><div id="comment-tools-30668" class="comment-tools"></div><div class="clear"></div><div id="comment-30668-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30513"></span>

<div id="answer-container-30513" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30513-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30513-score" class="post-score" title="current number of votes">2</div><span id="post-30513-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Be sure to follow <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.plugins;h=e60179d9e8aceb53796fdc2081a85707f41fb862;hb=refs/heads/master-1.10">doc/README.plugins</a> carefully.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '14, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-30513" class="comments-container"><span id="30575"></span><div id="comment-30575" class="comment"><div id="post-30575-score" class="comment-score"></div><div class="comment-text"><p>In the epan/Makefile.am for WS_1.10.5, it lists plugins/giop/packet-cosnaming.c and packet-coseventcomm.c However, these files no longer exist in that location. They were moved to epan/dissectors I'm surprised there isn't some sort of error from that.</p></div><div id="comment-30575-info" class="comment-info"><span class="comment-age">(07 Mar '14, 11:12)</span> <span class="comment-user userinfo">tlann</span></div></div><span id="30592"></span><div id="comment-30592" class="comment"><div id="post-30592-score" class="comment-score">1</div><div class="comment-text"><p>You are correct; however, the items you mention are under 'if ENABLE_STATIC' which I believe is only TRUE when building a "static" version of Wireshark.</p><p>Based upon the files mentioned under the 'if ...' it would seem no one has tried building a static version of Wireshark in quite some time.</p><p>Please file a bug at bugs.wireshark.org.</p><p>Thanks</p></div><div id="comment-30592-info" class="comment-info"><span class="comment-age">(07 Mar '14, 18:17)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-30513" class="comment-tools"></div><div class="clear"></div><div id="comment-30513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


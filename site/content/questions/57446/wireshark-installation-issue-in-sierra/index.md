+++
type = "question"
title = "Wireshark installation issue in Sierra"
description = '''Wireshark is not installing in sierra machine (v10.12.1) mac OS. How to install it?? It is throwing error to contact manufacturer, how to fix? (tried versions v2.0.x, v2.2.x of wireshark). '''
date = "2016-11-18T07:33:00Z"
lastmod = "2016-12-10T01:42:00Z"
weight = 57446
keywords = [ "sierra", "macosx", "installation" ]
aliases = [ "/questions/57446" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark installation issue in Sierra](/questions/57446/wireshark-installation-issue-in-sierra)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57446-score" class="post-score" title="current number of votes">0</div><span id="post-57446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark is not installing in sierra machine (v10.12.1) mac OS. How to install it?? It is throwing error to contact manufacturer, how to fix? (tried versions v2.0.x, v2.2.x of wireshark).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sierra" rel="tag" title="see questions tagged &#39;sierra&#39;">sierra</span> <span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '16, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/061c173cf5f3a7be949477e24d66b8a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PAVAN3215&#39;s gravatar image" /><p><span>PAVAN3215</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PAVAN3215 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Nov '16, 16:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-57446" class="comments-container"></div><div id="comment-tools-57446" class="comment-tools"></div><div class="clear"></div><div id="comment-57446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="57450"></span>

<div id="answer-container-57450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57450-score" class="post-score" title="current number of votes">0</div><span id="post-57450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is this a new install? Then this could be <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13152">this bug</a></p><p>I would guess a workaround is creating <code>/etc/paths.d</code> and <code>/etc/manpaths.d</code> directories by hand before installing, but YMMV so keep an eye on the bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Nov '16, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-57450" class="comments-container"><span id="57451"></span><div id="comment-57451" class="comment"><div id="post-57451-score" class="comment-score"></div><div class="comment-text"><p>I was having the same problem. /etc/paths.d existed but /etc/manpaths.d did not. Creating /etc/manpaths.d manually allowed the installation to complete successfully</p></div><div id="comment-57451-info" class="comment-info"><span class="comment-age">(18 Nov '16, 09:05)</span> <span class="comment-user userinfo">Bruno Wollmann</span></div></div><span id="57511"></span><div id="comment-57511" class="comment"><div id="post-57511-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the response, it fixed the issue in sierra 10.12.1</p><p>And in sierra v10.12, facing some sandbox issue , can i get the reason what it is exactly?</p><p>Creating those paths didn't resolve me the issue . Here is the install.log details from system : (also checked with v2.0.0 but installation failed with same error)</p><pre><code>Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installd[517]: PackageKit: prevent user idle system sleep
Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installd[517]: PackageKit: suspending backupd
Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installd[517]: PackageKit: releasing backupd
Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installd[517]: PackageKit: allow user idle system sleep
Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installd[517]: PackageKit: Install Failed: Error Domain=NSPOSIXErrorDomain Code=2 &quot;No such file or directory&quot; UserInfo={NSFilePath=/private/tmp/PKInstallSandbox.XXXXXX} {
            NSFilePath = &quot;/private/tmp/PKInstallSandbox.XXXXXX&quot;;
        }
Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installer[36664]: install:didFailWithError:Error Domain=NSPOSIXErrorDomain Code=2 &quot;No such file or directory&quot; UserInfo={NSFilePath=/private/tmp/PKInstallSandbox.XXXXXX}
Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installd[517]: PackageKit: Removing client PKInstallDaemonClient pid=36664, uid=0 (/usr/sbin/installer)
Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installd[517]: PackageKit: Running idle tasks
Nov 21 09:19:40 sp-el-capitan-10-11-FR-3 installd[517]: PackageKit: Done with sandbox removals
Nov 21 09:19:41 sp-el-capitan-10-11-FR-3 installer[36664]: Install failed: The Installer encountered an error that caused the installation to fail. Contact the software manufacturer for assistance.</code></pre></div><div id="comment-57511-info" class="comment-info"><span class="comment-age">(20 Nov '16, 20:03)</span> <span class="comment-user userinfo">PAVAN3215</span></div></div></div><div id="comment-tools-57450" class="comment-tools"></div><div class="clear"></div><div id="comment-57450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57988"></span>

<div id="answer-container-57988" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57988-score" class="post-score" title="current number of votes">-1</div><span id="post-57988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark requires XQuartz to run. It can be found <a href="https://www.xquartz.org">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '16, 00:43</strong></p><img src="https://secure.gravatar.com/avatar/fb6d430524bf9a0565423a4e77f83d0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JinOhChoi&#39;s gravatar image" /><p><span>JinOhChoi</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JinOhChoi has no accepted answers">0%</span></p></div></div><div id="comments-container-57988" class="comments-container"><span id="57989"></span><div id="comment-57989" class="comment"><div id="post-57989-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 2.x - which is what they're asking about - does <em>NOT</em> require XQuartz to run on Mac OS X/OS X/macOS; it's built using Qt, which supports Quartz natively.</p></div><div id="comment-57989-info" class="comment-info"><span class="comment-age">(10 Dec '16, 01:42)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-57988" class="comment-tools"></div><div class="clear"></div><div id="comment-57988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


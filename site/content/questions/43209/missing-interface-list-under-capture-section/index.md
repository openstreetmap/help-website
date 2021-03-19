+++
type = "question"
title = "Missing interface list under &quot;Capture&quot; section"
description = '''I have upgraded a user to Wireshark 1.12.5 and he now he does not have anything listed under the &quot;Capture&quot; section on the left side of the application. The app is missing the &quot;Interface List&quot; and &quot;Start&quot; buttons now. Does anyone know why this is? Thanks very much for any help on this issue!'''
date = "2015-06-16T09:01:00Z"
lastmod = "2015-06-19T09:26:00Z"
weight = 43209
keywords = [ "interface" ]
aliases = [ "/questions/43209" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Missing interface list under "Capture" section](/questions/43209/missing-interface-list-under-capture-section)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43209-score" class="post-score" title="current number of votes">0</div><span id="post-43209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have upgraded a user to Wireshark 1.12.5 and he now he does not have anything listed under the "Capture" section on the left side of the application. The app is missing the "Interface List" and "Start" buttons now. Does anyone know why this is?</p><p>Thanks very much for any help on this issue!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '15, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/1874987e18cf7e801e283b02809de418?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Irishbug&#39;s gravatar image" /><p><span>Irishbug</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Irishbug has no accepted answers">0%</span></p></div></div><div id="comments-container-43209" class="comments-container"><span id="43222"></span><div id="comment-43222" class="comment"><div id="post-43222-score" class="comment-score"></div><div class="comment-text"><p>OS and it's version?</p></div><div id="comment-43222-info" class="comment-info"><span class="comment-age">(16 Jun '15, 14:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43270"></span><div id="comment-43270" class="comment"><div id="post-43270-score" class="comment-score"></div><div class="comment-text"><p>Windows 7, 64 bit, Pro</p></div><div id="comment-43270-info" class="comment-info"><span class="comment-age">(17 Jun '15, 08:55)</span> <span class="comment-user userinfo">Irishbug</span></div></div><span id="43273"></span><div id="comment-43273" class="comment"><div id="post-43273-score" class="comment-score"></div><div class="comment-text"><p>What does <code>C:\Program Files\Wireshark\dumpcap.exe -D -M</code> (adjust the path to fit wherever you actually installed wireshark to) show?</p></div><div id="comment-43273-info" class="comment-info"><span class="comment-age">(17 Jun '15, 09:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="43276"></span><div id="comment-43276" class="comment"><div id="post-43276-score" class="comment-score"></div><div class="comment-text"><p>it lists my NIC</p></div><div id="comment-43276-info" class="comment-info"><span class="comment-age">(17 Jun '15, 11:01)</span> <span class="comment-user userinfo">Irishbug</span></div></div><span id="43304"></span><div id="comment-43304" class="comment"><div id="post-43304-score" class="comment-score"></div><div class="comment-text"><blockquote><p>it lists <strong>my</strong> NIC</p></blockquote><p>Just to be absolutely sure. You say it lists "my" NIC, while you are reporting the problem for the system of a user.</p><p>Did you run dumpcap on the users system (without admin privileges) and it printed the whole interface list?</p></div><div id="comment-43304-info" class="comment-info"><span class="comment-age">(17 Jun '15, 23:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-43209" class="comment-tools"></div><div class="clear"></div><div id="comment-43209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="43288"></span>

<div id="answer-container-43288" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43288-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43288-score" class="post-score" title="current number of votes">1</div><span id="post-43288-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so it seems WinPCap is working. I wondered if the initial WinPCap query made by Wireshark at startup to display the interface data that's missing had hung for some reason.</p><p>Have you rebooted since the install? Maybe try uninstalling Wireshark (and WinPCap) and installing again.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 15:08</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-43288" class="comments-container"><span id="43374"></span><div id="comment-43374" class="comment"><div id="post-43374-score" class="comment-score"></div><div class="comment-text"><p>I went ahead and reinstalled both apps and its working now, thanks!</p></div><div id="comment-43374-info" class="comment-info"><span class="comment-age">(19 Jun '15, 08:59)</span> <span class="comment-user userinfo">Irishbug</span></div></div><span id="43378"></span><div id="comment-43378" class="comment"><div id="post-43378-score" class="comment-score"></div><div class="comment-text"><p>I've converted my comment to an answer as that seems to have been the solution. Can you accept the answer with the checkmark icon?</p></div><div id="comment-43378-info" class="comment-info"><span class="comment-age">(19 Jun '15, 09:26)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-43288" class="comment-tools"></div><div class="clear"></div><div id="comment-43288-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43290"></span>

<div id="answer-container-43290" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43290-score" class="post-score" title="current number of votes">0</div><span id="post-43290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are your users part of a group (e.g. wireshark group)? If not you will have to add him. Check the following link for this situation <a href="https://wiki.wireshark.org/CaptureSetup/CapturePrivileges">https://wiki.wireshark.org/CaptureSetup/CapturePrivileges</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/9ee914a9fba57513c2612c9d2735a862?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cyverzek&#39;s gravatar image" /><p><span>cyverzek</span><br />
<span class="score" title="10 reputation points">10</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cyverzek has no accepted answers">0%</span></p></div></div><div id="comments-container-43290" class="comments-container"><span id="43294"></span><div id="comment-43294" class="comment"><div id="post-43294-score" class="comment-score"></div><div class="comment-text"><p>He's using Windows, so that doesn't apply.</p></div><div id="comment-43294-info" class="comment-info"><span class="comment-age">(17 Jun '15, 20:34)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-43290" class="comment-tools"></div><div class="clear"></div><div id="comment-43290-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43295"></span>

<div id="answer-container-43295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43295-score" class="post-score" title="current number of votes">0</div><span id="post-43295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to: CAPTURE OPTIONS | MANAGE INTERFACES | LOCAL INTERFACES</p><p>Make sure none of your interfaces have a check in the HIDE box.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 20:51</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-43295" class="comments-container"></div><div id="comment-tools-43295" class="comment-tools"></div><div class="clear"></div><div id="comment-43295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


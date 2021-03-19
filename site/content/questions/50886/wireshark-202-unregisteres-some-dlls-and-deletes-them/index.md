+++
type = "question"
title = "Wireshark 2.0.2 unregisteres some dlls and deletes them."
description = '''Hello,  I installed Wireshark as standard installation with simple deployment. I used standard switches to install it with default settings. I have question why installed unregisters and deletes dlls from Microsoft C++ redist ? Version doesn&#x27;t matter becasue I have installed MSVCP from 2005 to 2015....'''
date = "2016-03-14T05:17:00Z"
lastmod = "2016-03-22T05:31:00Z"
weight = 50886
keywords = [ "mfc120u.dll", "messdll", "deletedll", "wireshark" ]
aliases = [ "/questions/50886" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.0.2 unregisteres some dlls and deletes them.](/questions/50886/wireshark-202-unregisteres-some-dlls-and-deletes-them)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50886-score" class="post-score" title="current number of votes">0</div><span id="post-50886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I installed Wireshark as standard installation with simple deployment. I used standard switches to install it with default settings. I have question why installed unregisters and deletes dlls from Microsoft C++ redist ? Version doesn't matter becasue I have installed MSVCP from 2005 to 2015. Mainly is doing some mess with Redist.</p><p>For example it unregisters mfc120u.dll and deletes it. After computer reboot or relog I have message box about missing dll.</p><p>How to preserve this action?</p><p>I have read another thread regarding dll - about plugins - <a href="https://ask.wireshark.org/questions/41476/missing-dll">https://ask.wireshark.org/questions/41476/missing-dll</a> Here is spoken about that specific version of wireshark must be built with plugins with specific msvcp version.</p><p>It's not good for me, because for security reasons I cannot allow installer to delete some files.</p><p>What do you think?</p><p>Thx Darx</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mfc120u.dll" rel="tag" title="see questions tagged &#39;mfc120u.dll&#39;">mfc120u.dll</span> <span class="post-tag tag-link-messdll" rel="tag" title="see questions tagged &#39;messdll&#39;">messdll</span> <span class="post-tag tag-link-deletedll" rel="tag" title="see questions tagged &#39;deletedll&#39;">deletedll</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '16, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/6e15f7fc21f289b5a899dadf30747659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Darx&#39;s gravatar image" /><p><span>Darx</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Darx has no accepted answers">0%</span></p></div></div><div id="comments-container-50886" class="comments-container"><span id="50888"></span><div id="comment-50888" class="comment"><div id="post-50888-score" class="comment-score"></div><div class="comment-text"><p>Also i forgot to write: this appears randomly. I have other machine and this problem wasn't spotted with similar configuration (I mean MSVCPs)</p></div><div id="comment-50888-info" class="comment-info"><span class="comment-age">(14 Mar '16, 05:19)</span> <span class="comment-user userinfo">Darx</span></div></div></div><div id="comment-tools-50886" class="comment-tools"></div><div class="clear"></div><div id="comment-50886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50889"></span>

<div id="answer-container-50889" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50889-score" class="post-score" title="current number of votes">0</div><span id="post-50889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When installed, Wireshark launches Microsoft Visual C++ 2013 Redistributable (x64 or x86 depending on the version used) with the following flags: '/quiet /norestart'. It does not uninstall anything by itself, so it means that this comes from Microsoft redistributable installer itself.</p><p>As Wireshark uses the latest version provided by Microsoft, Im' not sure whether we can do something on our side or not...</p><p>BTW are you installing the x86 or x64 version?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '16, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Mar '16, 06:01</strong> </span></p></div></div><div id="comments-container-50889" class="comments-container"><span id="50890"></span><div id="comment-50890" class="comment"><div id="post-50890-score" class="comment-score"></div><div class="comment-text"><p>Thank you Pascal for reply, I will check if the version which I use is the latest. But I don't think so - I cannot let installer do what it wants, is it possible to disable MSVCP* installation via switch or something? Those libraries I can update manually. This is against our security policy which doesn't allow automatic updates.</p><p>Thanks :)</p></div><div id="comment-50890-info" class="comment-info"><span class="comment-age">(14 Mar '16, 06:05)</span> <span class="comment-user userinfo">Darx</span></div></div><span id="50891"></span><div id="comment-50891" class="comment"><div id="post-50891-score" class="comment-score"></div><div class="comment-text"><p>I am installing x64 versions :) again I forgot answer the question. Is here edit button? I can't see it</p></div><div id="comment-50891-info" class="comment-info"><span class="comment-age">(14 Mar '16, 06:07)</span> <span class="comment-user userinfo">Darx</span></div></div><span id="50892"></span><div id="comment-50892" class="comment"><div id="post-50892-score" class="comment-score"></div><div class="comment-text"><p>I'm googling right now to see if this is a known issue... But did not find anything so far.</p></div><div id="comment-50892-info" class="comment-info"><span class="comment-age">(14 Mar '16, 06:17)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="50893"></span><div id="comment-50893" class="comment"><div id="post-50893-score" class="comment-score"></div><div class="comment-text"><p>Thanks, maybe people or users have those packages up to date.</p></div><div id="comment-50893-info" class="comment-info"><span class="comment-age">(14 Mar '16, 06:19)</span> <span class="comment-user userinfo">Darx</span></div></div><span id="51084"></span><div id="comment-51084" class="comment"><div id="post-51084-score" class="comment-score"></div><div class="comment-text"><p><span>@Pascal Quantin</span> , did you find something ?</p></div><div id="comment-51084-info" class="comment-info"><span class="comment-age">(22 Mar '16, 05:30)</span> <span class="comment-user userinfo">Darx</span></div></div><span id="51085"></span><div id="comment-51085" class="comment not_top_scorer"><div id="post-51085-score" class="comment-score"></div><div class="comment-text"><p>Not for now.</p></div><div id="comment-51085-info" class="comment-info"><span class="comment-age">(22 Mar '16, 05:31)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-50889" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-50889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


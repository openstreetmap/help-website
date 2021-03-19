+++
type = "question"
title = "Function of the 00:ca:fe OUI (unregistered)"
description = '''What is the function of the 00:ca:fe OUI? The IEEE look-up tool doesn&#x27;t show a owner: https://standards.ieee.org/develop/regauth/oui/public.html In my environment, I believe that an Avaya PBX (which I suspect is implemented as VMs atop the Xen Hypervisor) is sending frames using this OUI. e.g. 00:ca...'''
date = "2015-06-01T06:07:00Z"
lastmod = "2015-06-04T04:45:00Z"
weight = 42792
keywords = [ "unregstered", "oui", "00cafe" ]
aliases = [ "/questions/42792" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Function of the 00:ca:fe OUI (unregistered)](/questions/42792/function-of-the-00cafe-oui-unregistered)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42792-score" class="post-score" title="current number of votes">0</div><span id="post-42792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the function of the 00:ca:fe OUI?</p><p>The IEEE look-up tool doesn't show a owner: <a href="https://standards.ieee.org/develop/regauth/oui/public.html">https://standards.ieee.org/develop/regauth/oui/public.html</a></p><p>In my environment, I believe that an Avaya PBX (which I suspect is implemented as VMs atop the Xen Hypervisor) is sending frames using this OUI. e.g. 00:ca:fe:01:97:65 and 00:ca:fe:46:13:32 [It also sends frames using a Xen-registered OUI and an Avaya-registered OUI.]</p><p>This smells like an error to me -- seems to me that no device wants to send frames using an unregistered OUI. On the other hand '00:ca:fe' seems like a human picked it -- the similarity to the French term 'cafe', its association with coffee, and the wide-spread (in languages other than French) use of the term.</p><p>?</p><p>--sk</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-unregstered" rel="tag" title="see questions tagged &#39;unregstered&#39;">unregstered</span> <span class="post-tag tag-link-oui" rel="tag" title="see questions tagged &#39;oui&#39;">oui</span> <span class="post-tag tag-link-00cafe" rel="tag" title="see questions tagged &#39;00cafe&#39;">00cafe</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '15, 06:07</strong></p><img src="https://secure.gravatar.com/avatar/18ae5b8bfddad49931ec557b9342075a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skendric&#39;s gravatar image" /><p><span>skendric</span><br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skendric has no accepted answers">0%</span></p></div></div><div id="comments-container-42792" class="comments-container"></div><div id="comment-tools-42792" class="comment-tools"></div><div class="clear"></div><div id="comment-42792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="42795"></span>

<div id="answer-container-42795" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42795-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42795-score" class="post-score" title="current number of votes">0</div><span id="post-42795-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looks handpicked to me, too. Maybe someone set it by hand; it's not unheard of that admins sometimes do this for various reasons (fun, keeping it persistent in multiple locations, easy recognition in capture, etc). The only way to be sure is to find the admin of the device and ask.</p><p>BTW, TraceWrangler also sets unused OUIs when sanitizing frames, especially because they are officially unused and cannot be linked to anyone ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42795" class="comments-container"></div><div id="comment-tools-42795" class="comment-tools"></div><div class="clear"></div><div id="comment-42795-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42802"></span>

<div id="answer-container-42802" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42802-score" class="post-score" title="current number of votes">0</div><span id="post-42802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If the MAC address is "human picked" then the administrator should have set the U/L bit as 1 for locally administered. Since the MAC address is 00, the U/L bit is not set and is available for an OUI.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 08:16</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-42802" class="comments-container"><span id="42803"></span><div id="comment-42803" class="comment"><div id="post-42803-score" class="comment-score"></div><div class="comment-text"><p>Right, the keyword being <strong>"should"</strong> :-)</p></div><div id="comment-42803-info" class="comment-info"><span class="comment-age">(01 Jun '15, 08:18)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="42804"></span><div id="comment-42804" class="comment"><div id="post-42804-score" class="comment-score"></div><div class="comment-text"><p>The management software should enforce this.</p></div><div id="comment-42804-info" class="comment-info"><span class="comment-age">(01 Jun '15, 08:28)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-42802" class="comment-tools"></div><div class="clear"></div><div id="comment-42802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42820"></span>

<div id="answer-container-42820" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42820-score" class="post-score" title="current number of votes">0</div><span id="post-42820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>At least according to the <a href="https://downloads.avaya.com/css/P8/documents/100148008">Military Unique Deployment Guide For (various pieces of Avaya hardware)</a>, it's something Avaya uses with Xen:</p><blockquote><p>On dom0: change file “<strong><em>/etc/xen/cm</em></strong>” to add virtual NIC (mybridge) to CM</p><p>a. The file will contain a line that looks something like this:</p><pre><code>     vif = [mac=00:CA:FE:27:43:37,bridge=avpublic]</code></pre></blockquote><p>(see section B1.7 "Enable Out of Band Management Interface").</p><p>The Google search that found that document also found other Avaya documents that speak of 00:ca:fe in MAC addresses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '15, 17:11</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '15, 17:12</strong> </span></p></div></div><div id="comments-container-42820" class="comments-container"><span id="42879"></span><div id="comment-42879" class="comment"><div id="post-42879-score" class="comment-score"></div><div class="comment-text"><p>Thanx folks, this gets me the info I was wanting</p><p>--sk</p></div><div id="comment-42879-info" class="comment-info"><span class="comment-age">(04 Jun '15, 04:45)</span> <span class="comment-user userinfo">skendric</span></div></div></div><div id="comment-tools-42820" class="comment-tools"></div><div class="clear"></div><div id="comment-42820-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


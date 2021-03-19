+++
type = "question"
title = "Protocol port change or port adding in wireshark"
description = '''In our product for LDAP we use 16110 as port along with default 389. SO everytime I need to &quot;decode as&quot; option. Is there any way to automatically decode the packets in this port? I see one option in Edit --&amp;gt; Preferences --&amp;gt; Protocol --&amp;gt; LDAP, here I think I can change the port number, but a...'''
date = "2012-09-12T10:15:00Z"
lastmod = "2012-09-14T23:52:00Z"
weight = 14213
keywords = [ "ldap" ]
aliases = [ "/questions/14213" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Protocol port change or port adding in wireshark](/questions/14213/protocol-port-change-or-port-adding-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14213-score" class="post-score" title="current number of votes">0</div><span id="post-14213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In our product for LDAP we use 16110 as port along with default 389. SO everytime I need to "decode as" option. Is there any way to automatically decode the packets in this port?</p><p>I see one option in Edit --&gt; Preferences --&gt; Protocol --&gt; LDAP, here I think I can change the port number, but anywhere I can add the port like - 389,16110 ?</p><p>Please clarify</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ldap" rel="tag" title="see questions tagged &#39;ldap&#39;">ldap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Sep '12, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/53003e4930d93213103c673c2fc87c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Santhosh%20Mohan&#39;s gravatar image" /><p><span>Santhosh Mohan</span><br />
<span class="score" title="0 reputation points">0</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Santhosh Mohan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '12, 19:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-14213" class="comments-container"><span id="14214"></span><div id="comment-14214" class="comment"><div id="post-14214-score" class="comment-score"></div><div class="comment-text"><p>I think SERVICES file should do it, not? It's in your Wireshark folder.</p></div><div id="comment-14214-info" class="comment-info"><span class="comment-age">(12 Sep '12, 11:34)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="14217"></span><div id="comment-14217" class="comment"><div id="post-14217-score" class="comment-score"></div><div class="comment-text"><p>Hansang, I doubt the services file will help. AFAIK it is used to do service name resolution, not for telling the dissectors on which port something is running at. But I might be wrong :-)</p></div><div id="comment-14217-info" class="comment-info"><span class="comment-age">(12 Sep '12, 12:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-14213" class="comment-tools"></div><div class="clear"></div><div id="comment-14213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="14289"></span>

<div id="answer-container-14289" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14289-score" class="post-score" title="current number of votes">3</div><span id="post-14289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>With version 1.8.x you can now save "Decode As..." definitions so that you don't have to re-enter them every time you start Wireshark.</p><p>Once you added one or more "Decode As..." definitions, go to "Analyze -&gt; User Defined Decodes..." and choose "Save". This will save these "Decode As..." definitions in your current configuration profile. So you can even have a different set of custom port mappings for different setups by defining multiple configuration profiles.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14289" class="comments-container"></div><div id="comment-tools-14289" class="comment-tools"></div><div class="clear"></div><div id="comment-14289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14218"></span>

<div id="answer-container-14218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14218-score" class="post-score" title="current number of votes">0</div><span id="post-14218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think you can add more than one port number here (which is different from what you can do at the HTTP dissector preferences). At least I have found no way to enter multiple ports.</p><p>You might want to open a feature request at the bug tracker at <a href="http://bugs.wireshark.org"></a><a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a>, but it will probably take some time for someone to be willing to take care of it.</p><p>The only other thing that comes to mind (and it is kinda thinking outside the box) is to use a packet anonymization tool like bittwiste or tcprewrite to change the port numbers in the trace file. It's an extra step, but you could automate it with a script.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '12, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-14218" class="comments-container"><span id="14221"></span><div id="comment-14221" class="comment"><div id="post-14221-score" class="comment-score"></div><div class="comment-text"><p>Oh, I got you. You're right, of course. Two different things.</p></div><div id="comment-14221-info" class="comment-info"><span class="comment-age">(12 Sep '12, 13:40)</span> <span class="comment-user userinfo">hansangb</span></div></div><span id="14225"></span><div id="comment-14225" class="comment"><div id="post-14225-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Jasper and hansangb. I will open a feature request in the bug tracker.</p></div><div id="comment-14225-info" class="comment-info"><span class="comment-age">(12 Sep '12, 21:54)</span> <span class="comment-user userinfo">Santhosh Mohan</span></div></div></div><div id="comment-tools-14218" class="comment-tools"></div><div class="clear"></div><div id="comment-14218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14285"></span>

<div id="answer-container-14285" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14285-score" class="post-score" title="current number of votes">0</div><span id="post-14285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should be able to accomplish this with <a href="http://wiki.wireshark.org/Lua">Lua</a>. I believe the very first example provided on the <a href="http://wiki.wireshark.org/Lua/Examples">Lua example page</a> is essentially what you'd need to do. Probably even easier/simpler/better is the example given under <a href="http://wiki.wireshark.org/LuaAPI/Dissector#DissectorTable">DissectorTable</a> in the Lua API documentation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '12, 19:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '12, 19:41</strong> </span></p></div></div><div id="comments-container-14285" class="comments-container"></div><div id="comment-tools-14285" class="comment-tools"></div><div class="clear"></div><div id="comment-14285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


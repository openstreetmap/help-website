+++
type = "question"
title = "Find IPhones and IPads"
description = '''Anyone have an suggestion on how to quickly identify IPhones or IPads? I have an applaince attached to a mirrored port so it sees all the traffic, including frmo the Wifi network. Is there a filter or something to quickly show these kind of devices?'''
date = "2011-03-22T20:17:00Z"
lastmod = "2011-03-25T10:28:00Z"
weight = 3036
keywords = [ "filtering" ]
aliases = [ "/questions/3036" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Find IPhones and IPads](/questions/3036/find-iphones-and-ipads)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3036-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Anyone have an suggestion on how to quickly identify IPhones or IPads? I have an applaince attached to a mirrored port so it sees all the traffic, including frmo the Wifi network. Is there a filter or something to quickly show these kind of devices?</p></div><div id="question-tags" class="tags-container tags">filtering</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '11, 20:17</strong></p><img src="https://secure.gravatar.com/avatar/16f4ef4f9271d3efbb0e92a10a2d9185?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gunnahafta&#39;s gravatar image" /><p>gunnahafta<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gunnahafta has no accepted answers">0%</span></p></div></div><div id="comments-container-3036" class="comments-container"></div><div id="comment-tools-3036" class="comment-tools"></div><div class="clear"></div><div id="comment-3036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="3065"></span>

<div id="answer-container-3065" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3065-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might want to filter on the User-Agent string, I just captured traffic from my iPhone and it gives the following User-Agent string:</p><pre><code>User-Agent: Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-us) 
   AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5</code></pre><p>So I guess the following filter might give you what you need:</p><pre><code>http.user_agent contains &quot;iPhone&quot; or http.user_agent contains &quot;iPad&quot;</code></pre><p>(I don't have an iPad yet, so I guessed the iPad part)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 15:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3065" class="comments-container"><span id="3075"></span><div id="comment-3075" class="comment"><div id="post-3075-score" class="comment-score"></div><div class="comment-text"><p>iPad User-Agent is (according to online sources):</p><p>Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10</p></div><div id="comment-3075-info" class="comment-info"><span class="comment-age">(23 Mar '11, 19:33)</span> wesmorgan1</div></div></div><div id="comment-tools-3065" class="comment-tools"></div><div class="clear"></div><div id="comment-3065-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3038"></span>

<div id="answer-container-3038" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3038-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try to spot those by MAC address vendor. The first 3 bytes of each 6 byte MAC address is vendor specific, and I'd assume that Apple has their devices registered to an Apple MAC (not entirely sure though, I have no iPhone/iPad to test this atm).</p><p>If you enable Name Resolution for the MAC Layer Wireshark will replace the first 3 bytes with the Vendor name taken from the file "manuf" in the Wireshark installation directory. Maybe that is enough to spot those devices.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3038" class="comments-container"></div><div id="comment-tools-3038" class="comment-tools"></div><div class="clear"></div><div id="comment-3038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3074"></span>

<div id="answer-container-3074" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3074-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You might also take a look at <a href="http://support.apple.com/kb/ts1629">"Well known TCP and UDP ports used by Apple software products"</a> - you might be able to catch a few by capturing Apple-specific protocol ports.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Mar '11, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-3074" class="comments-container"></div><div id="comment-tools-3074" class="comment-tools"></div><div class="clear"></div><div id="comment-3074-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3127"></span>

<div id="answer-container-3127" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3127-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To gunnahafta: Can you tell me how do you capture HTTP packet via your iphone?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/0d1f835bfa8cc91838057ef65fc4d1c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="A%20B&#39;s gravatar image" /><p>A B<br />
<span class="score" title="1 reputation points">1</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="A B has no accepted answers">0%</span></p></div></div><div id="comments-container-3127" class="comments-container"><span id="3134"></span><div id="comment-3134" class="comment"><div id="post-3134-score" class="comment-score"></div><div class="comment-text"><p>I don't think he's doing it via the iPhone itself, he captures on a mirrorport of a cabled device</p></div><div id="comment-3134-info" class="comment-info"><span class="comment-age">(25 Mar '11, 16:26)</span> Jasper ♦♦</div></div></div><div id="comment-tools-3127" class="comment-tools"></div><div class="clear"></div><div id="comment-3127-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


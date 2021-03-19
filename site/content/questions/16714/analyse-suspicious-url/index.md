+++
type = "question"
title = "Analyse suspicious url"
description = '''I got this suspicious URL in my mailbox of which I&#x27;m 99% sure that it&#x27;s not sent (intentionally in any case) by the person who is listed as the sender. Can I use Wireshark to analyse what this URL actually does without harming (downloading spyware, malware, cookies, ...) my computer in any way? Perh...'''
date = "2012-12-07T14:56:00Z"
lastmod = "2012-12-08T09:49:00Z"
weight = 16714
keywords = [ "url", "suspicious" ]
aliases = [ "/questions/16714" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Analyse suspicious url](/questions/16714/analyse-suspicious-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16714-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I got this suspicious URL in my mailbox of which I'm 99% sure that it's not sent (intentionally in any case) by the person who is listed as the sender. Can I use Wireshark to analyse what this URL actually does without harming (downloading spyware, malware, cookies, ...) my computer in any way? Perhaps by capturing my wlan device and running curl on this URL? If so, what should I be looking for specifically?</p><p>FYI, the URL is <span>hxxp://ashadtravels.com/data/default.php?ID=obucec&amp;catid=vupani</span></p><p>Comment: I modified your link from http:// to hxxp:// to prevent people from clicking on a link that night lead to malware.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">url suspicious</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '12, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/6f11e612bd6a521a7fe8bda78c161bf5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niefpaarschoenen&#39;s gravatar image" /><p>niefpaarscho...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niefpaarschoenen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '12, 15:03</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-16714" class="comments-container"></div><div id="comment-tools-16714" class="comment-tools"></div><div class="clear"></div><div id="comment-16714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16724"></span>

<div id="answer-container-16724" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16724-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you can use Wirehark to see what is transfered after calling the URL, but you can't prevent any harm with it. It's like having a camera to watch someone throwing something at a window. If it is a ping pong ball nothing will happen, but if it is a stone you can later tell/prove that it was - but the window is still broken.</p><p>The way of looking at an URL without fearing damage would be to use a virtual machine that you can reset to a previous snapshot. Or (maybe) a Intrusion Prevention System could catch the bad stuff and kill it before it hits. VM is usually the cheapest way to go if you want to take a look.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Dec '12, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16724" class="comments-container"><span id="16729"></span><div id="comment-16729" class="comment"><div id="post-16729-score" class="comment-score"></div><div class="comment-text"><p>And what kind of transfers should I be looking for? That is, how can I detect a stone with wireshark? Are there any useful/common filters for this type of detection?</p></div><div id="comment-16729-info" class="comment-info"><span class="comment-age">(08 Dec '12, 14:19)</span> niefpaarscho...</div></div><span id="16735"></span><div id="comment-16735" class="comment"><div id="post-16735-score" class="comment-score">1</div><div class="comment-text"><p>You can detect a stone if you know what a stone looks like. There are some filters out there to detect known malware signatures in packet traces, but most of them are so old that using them is basically useless. A lot of people still think that they can impress anyone by presenting filters for MS-Blaster or the Slammer worm, but these are completely irrelevant today.</p><p>IPS systems and virus scanners have more recent signatures, but usually there is nobody offering Wireshark filters for the latest (known) attacks. Unknown attacks will not be found in most cases anyway - or by pure luck.</p></div><div id="comment-16735-info" class="comment-info"><span class="comment-age">(09 Dec '12, 03:12)</span> Jasper ♦♦</div></div><span id="16737"></span><div id="comment-16737" class="comment"><div id="post-16737-score" class="comment-score"></div><div class="comment-text"><p>But there has to be some kind of file download and execution for a virus or malaware to operate, no? I thought that was basically the main difference in how Windows and Linux operate: Windows will execute some things automatically, while Linux will always ask. And is this download or execution not something that can be detected by Wireshark? Or in your analogy: maybe I cannot detect whether it's a stone that has been thrown, but I should be able to detect whether something was thrown at all, no?</p></div><div id="comment-16737-info" class="comment-info"><span class="comment-age">(09 Dec '12, 13:55)</span> niefpaarscho...</div></div><span id="16742"></span><div id="comment-16742" class="comment"><div id="post-16742-score" class="comment-score">1</div><div class="comment-text"><p>I'm sorry, but your facts about Windows and Linux are a little outdated - Windows (Vista and up) does ask about suspicious stuff if it falls into certain categories, and even Linux doesn't "always ask". Especially not if the attack is against the browser/java/etc.</p><p>But yes, you could see an executable being downloaded, but a lot of attacks are well hidden, e.g. inside scripts inside other content like pdf's or web pages. You need to know what you're looking for - it's not like you're going see something obvious like "infectvictim.exe" being downloaded.</p></div><div id="comment-16742-info" class="comment-info"><span class="comment-age">(10 Dec '12, 01:30)</span> Jasper ♦♦</div></div></div><div id="comment-tools-16724" class="comment-tools"></div><div class="clear"></div><div id="comment-16724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


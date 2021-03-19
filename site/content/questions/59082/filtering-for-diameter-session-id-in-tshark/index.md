+++
type = "question"
title = "Filtering for Diameter session ID in tshark"
description = '''dear team, in addition to above query, could you please help me to filter diameter messages in TSHARK using Session id.. i am able to display capyured diameter send &amp;amp; received messages in wireshark, i want to do the same in TSHARK in my script, but getting error as &quot;tshark: &quot;;&quot; was unexpected in...'''
date = "2017-01-26T11:31:00Z"
lastmod = "2017-01-26T12:20:00Z"
weight = 59082
keywords = [ "diameter", "tshark", "display-filter" ]
aliases = [ "/questions/59082" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering for Diameter session ID in tshark](/questions/59082/filtering-for-diameter-session-id-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59082-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>dear team, in addition to above query, could you please help me to filter diameter messages in TSHARK using Session id..</p><p>i am able to display capyured diameter send &amp; received messages in wireshark, i want to do the same in TSHARK in my script, but getting error as "tshark: ";" was unexpected in this context."</p><p>tshark.exe -r dia.pcap -V "diameter.Session-Id == "MMEC78.MMEGI8024.MME.EPC.MNC007.MCC404.3GPPNETWORK.ORG;3332250302;92145410;mme""</p><p>error: tshark: ";" was unexpected in this context.</p><p>please suggest.</p></div><div id="question-tags" class="tags-container tags">diameter tshark display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '17, 11:31</strong></p><img src="https://secure.gravatar.com/avatar/746454f41d14403415dece210aba20d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sudheer628&#39;s gravatar image" /><p>sudheer628<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sudheer628 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 26 Jan '17, 11:36</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-59082" class="comments-container"><span id="59083"></span><div id="comment-59083" class="comment"><div id="post-59083-score" class="comment-score"></div><div class="comment-text"><p>I converted your Answer to <a href="https://ask.wireshark.org/questions/19543/automatically-showing-replies-for-diameter-protocol-when-using-display-filter">this question</a> to a new question. This is a Q&amp;A site, not a forum--please see the FAQ.</p></div><div id="comment-59083-info" class="comment-info"><span class="comment-age">(26 Jan '17, 11:37)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-59082" class="comment-tools"></div><div class="clear"></div><div id="comment-59082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59084"></span>

<div id="answer-container-59084" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59084-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have to escape the inner double quotes:</p><pre><code>tshark.exe -r dia.pcap -V &quot;diameter.Session-Id == \&quot;MMEC78.MMEGI8024.MME.EPC.MNC007.MCC404.3GPPNETWORK.ORG;3332250302;92145410;mme\&quot;&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jan '17, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-59084" class="comments-container"><span id="59085"></span><div id="comment-59085" class="comment"><div id="post-59085-score" class="comment-score"></div><div class="comment-text"><p>Thanks Uli.. it works.. could you help related query.. i want to filter diamter user name, it works in wireshark but i get nothing in tshark (not even a error), reason is that tshark is not reading AVP: user-name message, which contains my IMSI (its LTE Mobile trace).</p><p>tshark filter used: tshark.exe -r dia.pcap -V "diameter.User-Name == "404071610557333""</p><p>kindly help..</p></div><div id="comment-59085-info" class="comment-info"><span class="comment-age">(26 Jan '17, 12:47)</span> sudheer628</div></div><span id="59088"></span><div id="comment-59088" class="comment"><div id="post-59088-score" class="comment-score"></div><div class="comment-text"><p>Looks like the same reason: escape the inner quotes?</p><p>tshark.exe -r dia.pcap -V "diameter.User-Name == \"404071610557333\""</p></div><div id="comment-59088-info" class="comment-info"><span class="comment-age">(26 Jan '17, 13:32)</span> Uli</div></div><span id="60036"></span><div id="comment-60036" class="comment"><div id="post-60036-score" class="comment-score"></div><div class="comment-text"><p>Not sure if your issue was resolved. I want to add here that tshark.exe -r dia.pcap -R "diameter.User-Name == 404071610557333" -O diameter command shall provide you desired results. Besides I you to use latest wireshark app as and when you can.</p></div><div id="comment-60036-info" class="comment-info"><span class="comment-age">(13 Mar '17, 10:04)</span> Vijay Gharge</div></div></div><div id="comment-tools-59084" class="comment-tools"></div><div class="clear"></div><div id="comment-59084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


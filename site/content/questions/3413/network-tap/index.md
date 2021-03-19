+++
type = "question"
title = "network tap"
description = '''Hi, I see mention of using a network tap many places, but I haven&#x27;t found anywhere to purchase one. Can somebody make a recommendation based on good personal experience? Thanks.'''
date = "2011-04-09T19:15:00Z"
lastmod = "2013-10-21T07:21:00Z"
weight = 3413
keywords = [ "tap" ]
aliases = [ "/questions/3413" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [network tap](/questions/3413/network-tap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3413-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I see mention of using a network tap many places, but I haven't found anywhere to purchase one. Can somebody make a recommendation based on good personal experience?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">tap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '11, 19:15</strong></p><img src="https://secure.gravatar.com/avatar/7df3f9a4b16eae9f77feb6eabe92919e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eelarry&#39;s gravatar image" /><p>eelarry<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eelarry has no accepted answers">0%</span></p></div></div><div id="comments-container-3413" class="comments-container"></div><div id="comment-tools-3413" class="comment-tools"></div><div class="clear"></div><div id="comment-3413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3416"></span>

<div id="answer-container-3416" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3416-score" class="post-score" title="current number of votes">6</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are a number of vendors that sell those, and I have personally used TAPs from those vendors:</p><ol><li>Netoptics - <a href="http://www.netoptics.com">www.netoptics.com</a></li><li>Datacom - <a href="http://www.datacomsystems.com/">www.datacomsystems.com</a></li><li>Finisar - <a href="http://www.finisar.com">www.finisar.com</a>, not sure if they still sell taps, doesn't look like they do</li></ol><p>Then there are others, which I haven't tested myself:</p><ol><li>Gigamon - <a href="http://www.gigamon.com/">www.gigamon.com</a></li><li>VSS - <a href="http://www.vssmonitoring.com">www.vssmonitoring.com</a></li></ol><p>and probably a couple more I haven't even heard of yet. I think most taps just work fine, I usually use the very basic full duplex taps from Netoptics and Datacom. My rules of thumb in using taps:</p><ol><li>Test them before going into the field. You need to be sure they deliver correct results</li><li>Careful with link aggregation taps. I had two encounters with that kind of tap (once Datacom, once Netoptics) and they didn't work as expected. The Datacom tap put only about 10% of the real traffic on the output lines toward the analyzer, and the link was not even close to being half full (can't remember the model). Netoptics introduced CRC errors into a direct connection between a Cisco Switch and a Cisco router (it was an "iTap Triple-speed Port Aggregator" for Gigabit copper).</li><li>Add-On Rule to #2: network taps are like modern cars: the less electronic doing fancy things, the better - there's less to break or go wrong :-)</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Apr '11, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '11, 03:19</p></div></div><div id="comments-container-3416" class="comments-container"><span id="3417"></span><div id="comment-3417" class="comment"><div id="post-3417-score" class="comment-score"></div><div class="comment-text"><p>Thank you for such a great reply!</p></div><div id="comment-3417-info" class="comment-info"><span class="comment-age">(10 Apr '11, 08:00)</span> eelarry</div></div><span id="3418"></span><div id="comment-3418" class="comment"><div id="post-3418-score" class="comment-score"></div><div class="comment-text"><p>You're welcome! If you're happy with it you might accept it as an answer :-)</p></div><div id="comment-3418-info" class="comment-info"><span class="comment-age">(10 Apr '11, 08:05)</span> Jasper ♦♦</div></div><span id="3419"></span><div id="comment-3419" class="comment"><div id="post-3419-score" class="comment-score"></div><div class="comment-text"><p>Definitely! I finally noticed the check mark icon :-)</p></div><div id="comment-3419-info" class="comment-info"><span class="comment-age">(10 Apr '11, 08:09)</span> eelarry</div></div><span id="30295"></span><div id="comment-30295" class="comment"><div id="post-30295-score" class="comment-score"></div><div class="comment-text"><p>Ok, I have a question on this...I am recommending to my bosses that they invest in a tap. Ok, all is well in the land of milk and honey and I get 3/4 to use in the enterprise. But, I still need a capture tool/pc/laptop to plug into the tap to capture that traffic. What do people use? I've seen presentations from sharkfest about how poorly laptops perform, what do people use??</p></div><div id="comment-30295-info" class="comment-info"><span class="comment-age">(28 Feb '14, 19:11)</span> RTJ10</div></div></div><div id="comment-tools-3416" class="comment-tools"></div><div class="clear"></div><div id="comment-3416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13876"></span>

<div id="answer-container-13876" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13876-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is one from Netscout <a href="http://www.netscout.com/products/service_provider/nSAS/ngenius_switches/ngenius_1500_series/Pages/default.aspx">netscout tap</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '12, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/0cf7e05b14ad6662ecde4c327bb2c39f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harsha&#39;s gravatar image" /><p>Harsha<br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harsha has no accepted answers">0%</span></p></div></div><div id="comments-container-13876" class="comments-container"><span id="13878"></span><div id="comment-13878" class="comment"><div id="post-13878-score" class="comment-score"></div><div class="comment-text"><p>Use this link to find it on ebay <a href="http://www.ebay.com/sch/i.html?_nkw=tap&amp;_sacat=175698&amp;_odkw=&amp;_osacat=175698">http://www.ebay.com/sch/i.html?_nkw=tap&amp;_sacat=175698&amp;_odkw=&amp;_osacat=175698</a></p></div><div id="comment-13878-info" class="comment-info"><span class="comment-age">(24 Aug '12, 12:18)</span> Harsha</div></div></div><div id="comment-tools-13876" class="comment-tools"></div><div class="clear"></div><div id="comment-13876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26254"></span>

<div id="answer-container-26254" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26254-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>And also some from <a href="http://www.cubro.net">Cubro</a> they have also stupid ones :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '13, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/de61350034eac6d25ddb332f7e48b4ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chrisliom&#39;s gravatar image" /><p>chrisliom<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chrisliom has no accepted answers">0%</span></p></div></div><div id="comments-container-26254" class="comments-container"></div><div id="comment-tools-26254" class="comment-tools"></div><div class="clear"></div><div id="comment-26254-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


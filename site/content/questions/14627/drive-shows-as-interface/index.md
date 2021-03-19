+++
type = "question"
title = "Drive shows as interface?"
description = '''I&#x27;ve installed wireshark on a server running Windows Server 2008 R2 Sp 2 to diagnose some multicast issues with an application and in the list of interfaces that wireshark shows it includes a mapped network drive. The list of interfaces to select for capturing includes the following:  Physical NIC 1...'''
date = "2012-10-01T06:34:00Z"
lastmod = "2012-10-01T07:02:00Z"
weight = 14627
keywords = [ "nic", "drive" ]
aliases = [ "/questions/14627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Drive shows as interface?](/questions/14627/drive-shows-as-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14627-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've installed wireshark on a server running Windows Server 2008 R2 Sp 2 to diagnose some multicast issues with an application and in the list of interfaces that wireshark shows it includes a mapped network drive. The list of interfaces to select for capturing includes the following:</p><ol><li>Physical NIC 1</li><li>M:\</li><li>Physical NIC 2</li></ol><p>Any idea why? It's a real problem because the multicast transmissions from my application are going through this interface.</p></div><div id="question-tags" class="tags-container tags">nic drive</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '12, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/a264ebc194ca183a362b72a1dd486f73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy73&#39;s gravatar image" /><p>Guy73<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy73 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Oct '12, 06:37</p></div></div><div id="comments-container-14627" class="comments-container"></div><div id="comment-tools-14627" class="comment-tools"></div><div class="clear"></div><div id="comment-14627-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14628"></span>

<div id="answer-container-14628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14628-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you checked the Interface descriptions at Edit -&gt; Preferences -&gt; Capture -&gt; Edit Interfaces? There might be a Comment for the second interface saying "M:\". In that edit window you can enter a name for each interface if you like.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Oct '12, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Oct '12, 07:03</p></div></div><div id="comments-container-14628" class="comments-container"><span id="14673"></span><div id="comment-14673" class="comment"><div id="post-14673-score" class="comment-score"></div><div class="comment-text"><p>I checked the preferences section you referred to and cannot find anywhere in there where the adapter is named M.</p><p>In the network settings on the server it only list two network adapters but Wireshark list three. When I searched the registry for the HEX ID wireshark gives for the NIC it comes up with "Microsoft Failover Cluster Virtual Adapter"</p><p>I disabled clustering and tried running my application locally on one of the cluster nodes and still get the same problem.</p></div><div id="comment-14673-info" class="comment-info"><span class="comment-age">(03 Oct '12, 08:53)</span> Guy73</div></div><span id="14675"></span><div id="comment-14675" class="comment"><div id="post-14675-score" class="comment-score"></div><div class="comment-text"><p>This looks like a problem with the Microsoft cluster virtual adapter then. If I were you I'd open up a bug report at <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a>, including screen shots of the capture interface dialog and preferences section I mentioned.</p></div><div id="comment-14675-info" class="comment-info"><span class="comment-age">(03 Oct '12, 08:57)</span> Jasper ♦♦</div></div><span id="14677"></span><div id="comment-14677" class="comment"><div id="post-14677-score" class="comment-score"></div><div class="comment-text"><p>I'm missing something here, why is it a problem? Wireshark only captures on the interfaces you tell it to, it doesn't influence the traffic in any way (apart from the requests it may generate to resolve names).</p></div><div id="comment-14677-info" class="comment-info"><span class="comment-age">(03 Oct '12, 09:00)</span> grahamb ♦</div></div><span id="14679"></span><div id="comment-14679" class="comment"><div id="post-14679-score" class="comment-score"></div><div class="comment-text"><p>@grahamb: I took it as a problem because the original question mentioned that it is one - but you're right, if it is only that the NIC name is strange it should just be renamed as long as the capture works fine.</p></div><div id="comment-14679-info" class="comment-info"><span class="comment-age">(03 Oct '12, 09:05)</span> Jasper ♦♦</div></div></div><div id="comment-tools-14628" class="comment-tools"></div><div class="clear"></div><div id="comment-14628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Can I use subnets or hosts file for manual subnet member resolution?"
description = '''Situation: we have a host with a dynamic ip, e.g today 8.8.1.2, tomorrow 8.8.3.200. The subnet is the same 8.8.0.0/16. During the live capture we need to spot (notice) that we have one of the hosts belonging to 8.8.0.0/16 subnet. Can we specify the subnet in HOSTS or SUBNETS file (in wireshark direc...'''
date = "2012-02-23T22:10:00Z"
lastmod = "2012-02-26T03:47:00Z"
weight = 9189
keywords = [ "subnets", "address", "hosts", "resolution", "ip" ]
aliases = [ "/questions/9189" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I use subnets or hosts file for manual subnet member resolution?](/questions/9189/can-i-use-subnets-or-hosts-file-for-manual-subnet-member-resolution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9189-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Situation: we have a host with a dynamic ip, e.g today 8.8.1.2, tomorrow 8.8.3.200. The subnet is the same 8.8.0.0/16. During the live capture we need to spot (notice) that we have one of the hosts belonging to 8.8.0.0/16 subnet.<br />
Can we specify the subnet in HOSTS or SUBNETS file (in wireshark directory) for manual resolution of it ? I've tried to specify if in the HOSTS file</p><pre><code>8.8.*.* oursubnethost
8.8.. oursubnethost
8.8.?.? oursubnethost
8.8.0.0/16 oursubnethost</code></pre><p>, but it does not work...<br />
<a href="http://www.wiresharktraining.com/tips-1-20.html">There is</a> a display filter for this task... Tip #17: Subnet Filters Wireshark understands CIDR (classless interdomain routing) address definitions. If you want to create a display filter for all devices who's network address starts with 10.3, use the syntax ip.addr==10.3.0.0/16. Use CIDR definitions when filtering on a subnet.</p></div><div id="question-tags" class="tags-container tags">subnets address hosts resolution ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '12, 22:10</strong></p><img src="https://secure.gravatar.com/avatar/c241cfce7680c690b68422163a98c0d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="contradictor_&#39;s gravatar image" /><p>contradictor_<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="contradictor_ has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-9189" class="comments-container"></div><div id="comment-tools-9189" class="comment-tools"></div><div class="clear"></div><div id="comment-9189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="9199"></span>

<div id="answer-container-9199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9199-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't do this in the hosts file. According to the Wireshark help file (I've never done it), you can do this in the <em>subnets</em> file using the syntax "8.8.0.0/16 subnetname".</p><p>Note that this will only work as long as there is not an exact match from the hosts file or from DNS. If there is an exact match, that name will be displayed.</p><p>Why not just use the display filter? That seems like the quickest, easiest way to spot a host belonging to a particular subnet. If you use partial name resolution using the <em>subnets</em> file, you might not notice a host belonging to the subnet of interest during a live capture if there is a lot of other traffic and the display is scrolling quickly. If you apply the display filter, you <em>will</em> see the traffic from that subnet, since it will be the only traffic displayed.</p><p>Even in a saved capture file it might be hard to spot the host you're interested in if its traffic is mixed in with a lot of traffic from other subnets, unless you use a display filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '12, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-9199" class="comments-container"><span id="9200"></span><div id="comment-9200" class="comment"><div id="post-9200-score" class="comment-score"></div><div class="comment-text"><p>Thanks... I'm not waiting for a specific subnet host. I'm planning to make a list of around 50 subnets(giving a nickname to each) and want to instantly see the nickname when one of these 50 subnets appears."A lot of traffic" is already filtered out. And following display filter could do the job ip.addr==9.9.0.0/16 or ip.addr==8.8.0.0/16 or ip.addr==7.7.0.0/16 ... (specifing 50 subnets in one filter). Thanks again.</p></div><div id="comment-9200-info" class="comment-info"><span class="comment-age">(24 Feb '12, 15:03)</span> contradictor_</div></div><span id="9201"></span><div id="comment-9201" class="comment"><div id="post-9201-score" class="comment-score"></div><div class="comment-text"><p>If that's the case, then it sounds like the subnets file is exactly what you want. After I posted my answer, I was able to test, and it worked with no problems on the first try.</p></div><div id="comment-9201-info" class="comment-info"><span class="comment-age">(24 Feb '12, 16:05)</span> Jim Aragon</div></div><span id="9202"></span><div id="comment-9202" class="comment"><div id="post-9202-score" class="comment-score"></div><div class="comment-text"><p>It's true, that " this will only work as long as there is not an exact match from the hosts file or from DNS. If there is an exact match, that name will be displayed." So my assigned NICKNAMES for subnets do NOT appear, if wireshark can resolve from DNS =(</p></div><div id="comment-9202-info" class="comment-info"><span class="comment-age">(24 Feb '12, 19:56)</span> contradictor_</div></div></div><div id="comment-tools-9199" class="comment-tools"></div><div class="clear"></div><div id="comment-9199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9216"></span>

<div id="answer-container-9216" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9216-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's possible to generate a HOSTS file with (255x255=65025) 65025 entries like this</p><pre><code>8.8.0.1 oursubnethost
8.8.0.158 oursubnethost
8.8.0.254 oursubnethost
8.8.222.235 oursubnethost
8.8.254.111 oursubnethost</code></pre><p>Will this be too hard for wireshark to manage? The hardware is ok.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '12, 03:47</strong></p><img src="https://secure.gravatar.com/avatar/c241cfce7680c690b68422163a98c0d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="contradictor_&#39;s gravatar image" /><p>contradictor_<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="contradictor_ has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '12, 03:48</p></div></div><div id="comments-container-9216" class="comments-container"><span id="9221"></span><div id="comment-9221" class="comment"><div id="post-9221-score" class="comment-score">1</div><div class="comment-text"><p>Don't know. I haven't heard of anyone trying to use a Wireshark hosts file that large. Try it and let us know. Here's another possibility to highlight traffic from the systems you're interested in. Create a coloring rule and put it at the top of the coloring rule list. Something like "ip.src==8.8.0.0/16".</p></div><div id="comment-9221-info" class="comment-info"><span class="comment-age">(26 Feb '12, 10:19)</span> Jim Aragon</div></div></div><div id="comment-tools-9216" class="comment-tools"></div><div class="clear"></div><div id="comment-9216-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


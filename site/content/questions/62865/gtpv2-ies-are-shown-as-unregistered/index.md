+++
type = "question"
title = "GTPV2 IEs are shown as Unregistered"
description = '''Hi, I am building wireshark 2.2.4 in centOs6 using make uninstall, ./autogen.sh, ./configure, make clean, make, make install...  I changed packet-gtpv2.c by adding some new IEs. Now the problem is some of the new IEs are getting registered, some of not getting registered. And surprisingly some old I...'''
date = "2017-07-19T01:27:00Z"
lastmod = "2017-07-24T03:54:00Z"
weight = 62865
keywords = [ "gtpv2c", "dissector", "display", "malformed", "display-filter" ]
aliases = [ "/questions/62865" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GTPV2 IEs are shown as Unregistered](/questions/62865/gtpv2-ies-are-shown-as-unregistered)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62865-score" class="post-score" title="current number of votes">0</div><span id="post-62865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am building wireshark 2.2.4 in centOs6 using</p><pre><code>make uninstall,
./autogen.sh,
./configure,
make clean,
make,
make install...</code></pre><p>I changed packet-gtpv2.c by adding some new IEs. Now the problem is some of the new IEs are getting registered, some of not getting registered. And surprisingly some old IEs are also shown not registered. The failed assertion message is shown as (guint)hfindex&lt;gpa_hfinfo.len (Unregistered hf)... Any Idea about the issues? Any upper limit to add a new hf in hf_register_info in gtpv2.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gtpv2c" rel="tag" title="see questions tagged &#39;gtpv2c&#39;">gtpv2c</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-malformed" rel="tag" title="see questions tagged &#39;malformed&#39;">malformed</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '17, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/48912e037040264c21d2e543aca485e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abhisek&#39;s gravatar image" /><p><span>Abhisek</span><br />
<span class="score" title="16 reputation points">16</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abhisek has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Jul '17, 02:30</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-62865" class="comments-container"></div><div id="comment-tools-62865" class="comment-tools"></div><div class="clear"></div><div id="comment-62865-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62867"></span>

<div id="answer-container-62867" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62867-score" class="post-score" title="current number of votes">0</div><span id="post-62867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You are probably better off building the development version as new IEs has been added to the standard code since 2.2.4. What you are describing is probably a bug in your code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '17, 01:46</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-62867" class="comments-container"><span id="62868"></span><div id="comment-62868" class="comment"><div id="post-62868-score" class="comment-score"></div><div class="comment-text"><p>What i found that IEs are added but there dissection still not yet coded completely in packet-gtpv2.c. So basically I coded the dissectors. For that I follow usual method proto_tree_add_item(....) and added the hf to hf_register_info array. But after adding those hf, the assertion message (guint)hfindex&lt;gpa_hfinfo.len (Unregistered hf!) is shown for some of new as well as old hf. Basically Unregistered hf message will come is the hf is not added in hf_register_info array. But in this case though it's added, the error is shown.</p></div><div id="comment-62868-info" class="comment-info"><span class="comment-age">(19 Jul '17, 02:01)</span> <span class="comment-user userinfo">Abhisek</span></div></div><span id="62869"></span><div id="comment-62869" class="comment"><div id="post-62869-score" class="comment-score"></div><div class="comment-text"><p>If you enhance the dissector you should commit the code to the Wireshark project. It is impossible or at least hard to figure out what's wrong without seeing the code.</p></div><div id="comment-62869-info" class="comment-info"><span class="comment-age">(19 Jul '17, 02:20)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="62870"></span><div id="comment-62870" class="comment"><div id="post-62870-score" class="comment-score"></div><div class="comment-text"><p>I customised the code for internal purpose. Is it ok if I share the proto_register_gtpv2(....) function content.</p></div><div id="comment-62870-info" class="comment-info"><span class="comment-age">(19 Jul '17, 03:50)</span> <span class="comment-user userinfo">Abhisek</span></div></div><span id="62871"></span><div id="comment-62871" class="comment"><div id="post-62871-score" class="comment-score"></div><div class="comment-text"><p>It might suffice.</p></div><div id="comment-62871-info" class="comment-info"><span class="comment-age">(19 Jul '17, 04:38)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="62873"></span><div id="comment-62873" class="comment"><div id="post-62873-score" class="comment-score"></div><div class="comment-text"><p>I added the code snippet in answer part.</p></div><div id="comment-62873-info" class="comment-info"><span class="comment-age">(19 Jul '17, 04:48)</span> <span class="comment-user userinfo">Abhisek</span></div></div><span id="63042"></span><div id="comment-63042" class="comment not_top_scorer"><div id="post-63042-score" class="comment-score"></div><div class="comment-text"><p>I added IEs one by one and rebuilt every time, AND at the end GOT A CLEAN EXECUTABLE. What I am thinking that probably the error caused by adding any hf entry more than once in the</p><pre><code>hf_register_info</code></pre><p>array. Anyhow it's great learning...</p></div><div id="comment-63042-info" class="comment-info"><span class="comment-age">(24 Jul '17, 03:54)</span> <span class="comment-user userinfo">Abhisek</span></div></div></div><div id="comment-tools-62867" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-62867-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


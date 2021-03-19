+++
type = "question"
title = "EtherCAT sub-dissector in Lua"
description = '''Hi, I want to create an EtherCAT subdissector in Lua, to dissect the payload of the EtherCAT datagrams. Consulting the WireShark documentation didn&#x27;t help me out, I know how to build a custom (chain/post-) dissector in Lua but not how to dissect data of an existing protocol. Post- or Chain dissector...'''
date = "2013-09-17T19:31:00Z"
lastmod = "2014-03-15T09:03:00Z"
weight = 24876
keywords = [ "lua", "ethercat", "subdissector", "sub-dissector" ]
aliases = [ "/questions/24876" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [EtherCAT sub-dissector in Lua](/questions/24876/ethercat-sub-dissector-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24876-score" class="post-score" title="current number of votes">0</div><span id="post-24876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to create an EtherCAT subdissector in Lua, to dissect the payload of the EtherCAT datagrams. Consulting the WireShark documentation didn't help me out, I know how to build a custom (chain/post-) dissector in Lua but not how to dissect data of an existing protocol.</p><p>Post- or Chain dissectors allow me to dissect the data outside of the existing protocol, so my tree items are listed below the EtherCAT dataframes instead of expanding the ecat protocol.</p><p>In other words, I can do this:</p><pre><code>+ EtherCAT frame header
- EtherCAT datagram(s)
      - EtherCAT datagram 1
            + Header
            Data
      + EtherCAT datagram 2
+ My protocol</code></pre><p>But I want to do something like this:</p><pre><code>+ EtherCAT frame header
- EtherCAT datagram(s)
      - EtherCAT datagram 1
            + Header
            - Data
                  + My protocol
      + EtherCAT datagram 2</code></pre><p>On <a href="http://wiki.wireshark.org/Protocols/ethercat">WireShark EtherCAT protocol</a> they recommend using the <code>heur_dissector_add("ecat.data",..)</code> function, which seems to fulfill my purpose except that Lua does not accept this function.</p><p>Any ideas or tips on how to access and dissect <code>ecat.data</code> using a Lua script?</p><p>Best regards, Gerald</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-ethercat" rel="tag" title="see questions tagged &#39;ethercat&#39;">ethercat</span> <span class="post-tag tag-link-subdissector" rel="tag" title="see questions tagged &#39;subdissector&#39;">subdissector</span> <span class="post-tag tag-link-sub-dissector" rel="tag" title="see questions tagged &#39;sub-dissector&#39;">sub-dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '13, 19:31</strong></p><img src="https://secure.gravatar.com/avatar/57b93085a535373e73bac2c71695ff0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald&#39;s gravatar image" /><p><span>Gerald</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '13, 23:39</strong> </span></p></div></div><div id="comments-container-24876" class="comments-container"></div><div id="comment-tools-24876" class="comment-tools"></div><div class="clear"></div><div id="comment-24876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25020"></span>

<div id="answer-container-25020" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25020-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25020-score" class="post-score" title="current number of votes">0</div><span id="post-25020-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gerald has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>recommend using the heur_dissector_add("ecat.data",..) function, which seems to fulfill my purpose except that Lua does not accept this function.</p></blockquote><p>registering heuristic dissectors is not implemented for Lua, that's the reason you cannot do it.</p><p>Unless somebody (you or a Wireshark developer) implements that feature, your only option is to write the sub-dissector in C.</p><blockquote><p>Any ideas or tips on how to access and dissect ecat.data using a Lua script?</p></blockquote><p>You may try to use a post dissector. However I'm not sure if that will work with your problem. It depends on your requirements. Maybe you just try it.</p><blockquote><p><a href="http://wiki.wireshark.org/Lua">http://wiki.wireshark.org/Lua</a><br />
<a href="http://wiki.wireshark.org/Lua/Dissectors">http://wiki.wireshark.org/Lua/Dissectors</a><br />
<a href="http://wiki.wireshark.org/Lua/Examples/PostDissector">http://wiki.wireshark.org/Lua/Examples/PostDissector</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-25020" class="comments-container"><span id="25064"></span><div id="comment-25064" class="comment"><div id="post-25064-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer.</p><p>I hoped to avoid using C, but it seems Lua is not (yet) able to fulfill my requirements.</p><p>I tried using both a chained and a post dissector, but the results are the same. My dissection works perfectly, but only after the standard (in my case ecat) protocol/dissector. I cannot find a way to (sub-) dissect the 'ecat.data' field within the standard protocol/dissector.</p><p>Maybe I should give up on using Lua and try this in C.</p><p>Best regards, Gerald</p></div><div id="comment-25064-info" class="comment-info"><span class="comment-age">(21 Sep '13, 01:19)</span> <span class="comment-user userinfo">Gerald</span></div></div><span id="25065"></span><div id="comment-25065" class="comment"><div id="post-25065-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Maybe I should give up on using Lua and try this in C</p></blockquote><p>if you need a real sub-dissector (your description sounds like that), then yes.</p><p>You could also try to add sub-dissector support for Lua to Wireshark ;-)</p></div><div id="comment-25065-info" class="comment-info"><span class="comment-age">(21 Sep '13, 03:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-25020" class="comment-tools"></div><div class="clear"></div><div id="comment-25020-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30816"></span>

<div id="answer-container-30816" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30816-score" class="post-score" title="current number of votes">2</div><span id="post-30816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Heuristic dissector support for Lua scripts is now available in 1.11.3, in the latest <a href="http://www.wireshark.org/download/automated/">nightly builds</a>. This was added as part of enhancement <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9815">bug 9815</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '14, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span> </br></br></p></div></div><div id="comments-container-30816" class="comments-container"></div><div id="comment-tools-30816" class="comment-tools"></div><div class="clear"></div><div id="comment-30816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


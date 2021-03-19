+++
type = "question"
title = "How is elements of packet is inserted into tvb structure?"
description = '''Hi. With reference to this e-book chapter 8, page 430, Step 5: Create The Dissector, it is stated that &quot;The tvb structure is used to extract and decode the data contained in each element of the packet.&quot; And &quot;To acquire data from the packet, we used tvb_ get_ xxx functions.&quot; My question is, how is th...'''
date = "2011-08-03T22:24:00Z"
lastmod = "2011-08-04T19:24:00Z"
weight = 5480
keywords = [ "development" ]
aliases = [ "/questions/5480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How is elements of packet is inserted into tvb structure?](/questions/5480/how-is-elements-of-packet-is-inserted-into-tvb-structure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5480-score" class="post-score" title="current number of votes">1</div><span id="post-5480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>With reference to this <a href="http://comes.umy.ac.id/file.php/1/Pengumuman_FT/E-Book_TI/Wireshark_and_Ethereal.pdf">e-book</a> chapter 8, page 430, Step 5: Create The Dissector, it is stated that "The tvb structure is used to extract and decode the data contained in each element of the packet." And "To acquire data from the packet, we used tvb_ get_ xxx functions." My question is, how is the actual process of extracting data from each element of the packet take place, like how is the element is inserted into the tvb structure? What functions are involved and if it's possible, please provide an example. Thank you for your time.</p><p>Shuda.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '11, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/f51ef179a21149a3de347387e764978d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shuda&#39;s gravatar image" /><p><span>Shuda</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shuda has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Aug '11, 16:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-5480" class="comments-container"></div><div id="comment-tools-5480" class="comment-tools"></div><div class="clear"></div><div id="comment-5480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5493"></span>

<div id="answer-container-5493" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5493-score" class="post-score" title="current number of votes">2</div><span id="post-5493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Elements are not added in the TVB structure; the TVB contains the raw bytes of the packet (from the wire). Dissectors then take these bytes and create a human presentation of it.</p><p>They do this, typically, by calling proto_tree_add_item() (which takes the offset into the TVB and the length of the data as well as an hf field which describes the encoding of the data being retrieved). There are many other proto_tree_add_<em>() functions, if more control over the presentation is desired. Data can be retrieved from the TVB using the tvb_get_</em>() functions.</p><p>For examples, see any of the dissectors in the Wireshark source code (in the epan/dissectors/ directory).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '11, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-5493" class="comments-container"><span id="5516"></span><div id="comment-5516" class="comment"><div id="post-5516-score" class="comment-score"></div><div class="comment-text"><p>I see. Thanks for your reply! Really appreciate it. I will try to see the examples in the dissectors. =)</p></div><div id="comment-5516-info" class="comment-info"><span class="comment-age">(04 Aug '11, 19:24)</span> <span class="comment-user userinfo">Shuda</span></div></div></div><div id="comment-tools-5493" class="comment-tools"></div><div class="clear"></div><div id="comment-5493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


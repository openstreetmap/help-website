+++
type = "question"
title = "Dissecting bitfields larger than 32 bits"
description = '''I am writing a dissector for a protocol which contains bitfields that are larger than 32 bits. For instance there is one bitfield that is 48-bits long, with other bitfields being 80-bits long. Setting the bitmask for the field in the header_field_info structure does not work since the bitmask is onl...'''
date = "2013-04-18T16:12:00Z"
lastmod = "2013-04-21T13:56:00Z"
weight = 20599
keywords = [ "dissector" ]
aliases = [ "/questions/20599" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dissecting bitfields larger than 32 bits](/questions/20599/dissecting-bitfields-larger-than-32-bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20599-score" class="post-score" title="current number of votes">1</div><span id="post-20599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a dissector for a protocol which contains bitfields that are larger than 32 bits. For instance there is one bitfield that is 48-bits long, with other bitfields being 80-bits long. Setting the bitmask for the field in the <code>header_field_info</code> structure does not work since the bitmask is only 32-bits long.</p><p>I believe that there are a number of possible ways to proceed:</p><ol><li>I can extract the bytes from the tvb into local variables and extract the relevant bits for each field (possibly using bit accessors such as <code>tvb_get_bits64</code> where appropriate) and then use <code>proto_tree_add_text</code> to add the values to the display</li><li>Treat the bitfield in a similar way to compressed data and extract the bit fields into a new buffer as if they were byte aligned then use <code>tvb_new_real_data</code>, etc., to add a new data source and then dissect the new tvb buffer from offset 0</li></ol><p>Neither method will be as nice or as easy as using the inbuilt bitmask method. It would be nice to display the individual fields as the standard bitmask dissection (with the bit pattern preceding the field title and contents) but I cannot think of a nice way of doing this.</p><p>What are the pros and cons of these two methods and which should I choose? Is there another, better way to proceed that I haven't thought of?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '13, 16:12</strong></p><img src="https://secure.gravatar.com/avatar/247023f80d6f609bd463bfc0de374f06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GrahamS&#39;s gravatar image" /><p><span>GrahamS</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GrahamS has no accepted answers">0%</span></p></div></div><div id="comments-container-20599" class="comments-container"></div><div id="comment-tools-20599" class="comment-tools"></div><div class="clear"></div><div id="comment-20599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20688"></span>

<div id="answer-container-20688" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20688-score" class="post-score" title="current number of votes">0</div><span id="post-20688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd go with method 1 (using <code>proto_tree_add_text</code>). I used this method in a couple of dissectors I wrote some years ago for proprietary protocols. I don't remember why I didn't use the bitmask field in <code>header_field_info</code> - I probably wasn't aware of it at the time. But the obvious approach of a series of <code>proto_tree_add_text</code> calls protected by <code>if</code> statements, while more verbose, is straightforward, clean, and clear to maintainers. It's also easy to crank out the code with a regex search-and-replace or a piece of throwaway scripting, if you have a header that defines the various bits, for example.</p><p>I'm by no means an expert in this area, though, so take that with a pinch of salt.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '13, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/513295189ee24340b8de5822e630c627?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwojcik&#39;s gravatar image" /><p><span>mwojcik</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwojcik has no accepted answers">0%</span></p></div></div><div id="comments-container-20688" class="comments-container"></div><div id="comment-tools-20688" class="comment-tools"></div><div class="clear"></div><div id="comment-20688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


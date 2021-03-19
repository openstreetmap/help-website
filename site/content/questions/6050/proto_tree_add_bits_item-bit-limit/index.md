+++
type = "question"
title = "proto_tree_add_bits_item(), bit limit?"
description = '''I am trying to use proto_tree_add_bits_item() to select all the bits that are used in a 7-bit ASCII message of arbitrary length. I convert this 7-bit ASCII to 8-bit and then print out a string, but I would like Wireshark to select the bits that this string was derived from when the &quot;Packet Bytes&quot; wi...'''
date = "2011-09-01T12:10:00Z"
lastmod = "2011-09-01T17:07:00Z"
weight = 6050
keywords = [ "development", "dissector" ]
aliases = [ "/questions/6050" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [proto\_tree\_add\_bits\_item(), bit limit?](/questions/6050/proto_tree_add_bits_item-bit-limit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6050-score" class="post-score" title="current number of votes">0</div><span id="post-6050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to use <code>proto_tree_add_bits_item()</code> to select all the bits that are used in a 7-bit ASCII message of arbitrary length. I convert this 7-bit ASCII to 8-bit and then print out a string, but I would like Wireshark to select the bits that this string was derived from when the "Packet Bytes" window is in "Bits View" instead of the standard "Hex view". I have found that it will highlight the individual bits up to 7*3=21, and then it starts highlighting whole bytes. What's up?</p><pre><code>ti = proto_tree_add_bits_item(cftext_sub_tree3, hf_cftext_textmess, tvb, 1918, 7*num_char, FALSE);

/* I am not interested in printing the bits here,
 * that&#39;s why I am using proto_item_set_text() instead of
 * proto_item_append_text().
 */
proto_item_set_text(ti, &quot;Text Message: %s&quot;, ascii_message);</code></pre><p>Any ideas/answers are greatly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Sep '11, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/0f23fe6d24be5b22962647ce5a315725?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Techboy&#39;s gravatar image" /><p><span>Techboy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Techboy has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Sep '11, 14:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-6050" class="comments-container"><span id="6051"></span><div id="comment-6051" class="comment"><div id="post-6051-score" class="comment-score"></div><div class="comment-text"><p>You should indent your code four spaces so that it is correctly formatted. Unserscores, asterisks, and backticks are used to format posts. See the <a href="http://wiki.osqa.net/display/docs/OSQA+User%27s+Guide#OSQAUser%27sGuide-TheMarkdownLanguage">OSQA User's Guide</a> about markdown for more information.</p></div><div id="comment-6051-info" class="comment-info"><span class="comment-age">(01 Sep '11, 12:25)</span> <span class="comment-user userinfo">multipleinte...</span></div></div><span id="6053"></span><div id="comment-6053" class="comment"><div id="post-6053-score" class="comment-score"></div><div class="comment-text"><ol><li>To demonstrate the problem, can you add a screenshot to your question?</li><li>Is <code>num_char</code> set to 3 in your code above?</li><li>Does the incorrect highlighting occur only when you select the tree item added by <code>proto_tree_add_bits_item()</code> in the <em>Packet Bytes</em> window?</li></ol></div><div id="comment-6053-info" class="comment-info"><span class="comment-age">(01 Sep '11, 17:07)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-6050" class="comment-tools"></div><div class="clear"></div><div id="comment-6050-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>


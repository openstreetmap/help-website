+++
type = "question"
title = "What is a tap, and how do I use one with the Lua interface?"
description = '''I want to understand what is meant by &quot;tap&quot; in Lua API. Specifically, I would like clarification on the following:  How I can use a tap and what are the benefits?  What is resetting a tap? What is removing a tap?  What information is lost when the tap is reset or removed?  When is the information lo...'''
date = "2012-02-02T04:26:00Z"
lastmod = "2012-02-02T18:25:00Z"
weight = 8776
keywords = [ "development", "lua", "tap" ]
aliases = [ "/questions/8776" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is a tap, and how do I use one with the Lua interface?](/questions/8776/what-is-a-tap-and-how-do-i-use-one-with-the-lua-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8776-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8776-score" class="post-score" title="current number of votes">0</div><span id="post-8776-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to understand what is meant by "tap" in Lua API. Specifically, I would like clarification on the following:</p><ul><li>How I can use a tap and what are the benefits?<br />
</li><li>What is resetting a tap?</li><li>What is removing a tap?<br />
</li><li>What information is lost when the tap is reset or removed?<br />
</li><li>When is the information lost when the reset and remove functions are called?<br />
</li><li>What is the difference between these two functions?</li></ul></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '12, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p><span>Leena</span><br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Feb '12, 18:26</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></div></div><div id="comments-container-8776" class="comments-container"><span id="8778"></span><div id="comment-8778" class="comment"><div id="post-8778-score" class="comment-score">1</div><div class="comment-text"><p>Have you read <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.tapping">README.tapping</a> for some insights? It's C oriented, but talks about taps.</p></div><div id="comment-8778-info" class="comment-info"><span class="comment-age">(02 Feb '12, 05:18)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-8776" class="comment-tools"></div><div class="clear"></div><div id="comment-8776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8794"></span>

<div id="answer-container-8794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8794-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8794-score" class="post-score" title="current number of votes">1</div><span id="post-8794-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Jaap pointed out, the <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.tapping">README</a> is a great resource in understanding taps. The Wireshark User Manual also includes a page on taps (aka "<a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Listener.html#lua_class_Listener">Listener</a>") (but it's sadly sparse and actually outdated).</p><blockquote><p>What is resetting a tap?</p></blockquote><p><code>listener.reset()</code> is an interface function (or a callback) that Wireshark automatically calls as a notification to reset any state for the tap (e.g., counters). It's called on opening (and closing) a capture file or by the Refresh Button in Wireshark. If you don't maintain state, you don't need to implement this.</p><blockquote><p>What is removing a tap?</p></blockquote><p><code>listener.remove()</code> unregisters the tap thereby ending any subsequent calls to <code>listener.packet()</code>, <code>listener.reset()</code>, and <code>listener.draw()</code>. Why call it? Think of this as turning off the light when you leave the room. It's an important step to conserve resources in Wireshark.</p><blockquote><p>What information is lost when the tap is reset or removed?</p></blockquote><p>Short answer: "none"</p><p>By "information", I assume you mean some kind of state variable. No information is maintained by the tap. State variables would have to be declared outside of the tap. Therefore, destroying the tap has no effect on the state.</p><blockquote><p>When is the information lost when the reset and remove functions are called?</p></blockquote><p>N/A (see previous answer)</p><blockquote><p>What is the difference between these two functions?</p></blockquote><p>See above</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '12, 18:25</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></p></div></div><div id="comments-container-8794" class="comments-container"></div><div id="comment-tools-8794" class="comment-tools"></div><div class="clear"></div><div id="comment-8794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


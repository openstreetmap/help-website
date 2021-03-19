+++
type = "question"
title = "How to use the &quot;less than&quot; symbol in questions and answers?"
description = '''Every time I try to use the &amp;lt; (less than) or &amp;gt; (greater than) symbols, the output is never what I want. What&#x27;s the trick at using those symbols? For example, if I wanted to illustrate the tshark command of tshark -R &amp;lt; Read filter&amp;gt;, I can only do so if I ensure there&#x27;s at least once space...'''
date = "2016-07-27T14:06:00Z"
lastmod = "2016-07-27T14:45:00Z"
weight = 54380
keywords = [ "markdown", "osqa" ]
aliases = [ "/questions/54380" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to use the "less than" symbol in questions and answers?](/questions/54380/how-to-use-the-less-than-symbol-in-questions-and-answers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54380-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Every time I try to use the <code>&lt;</code> (less than) or <code>&gt;</code> (greater than) symbols, the output is never what I want. What's the trick at using those symbols?</p><p>For example, if I wanted to illustrate the <code>tshark</code> command of <code>tshark -R &lt; Read filter&gt;</code>, I can only do so if I ensure there's at least once space after the <code>&lt;</code> symbol. If I omit the space, then I end up with this: <code>tshark -R &lt;Read filter&gt;</code> ... which causes the text to not be displayed. I've tried searching the OSQA markdown syntax, such as at <a href="https://sourceforge.net/p/osqa-rus/discussion/markdown_syntax">https://sourceforge.net/p/osqa-rus/discussion/markdown_syntax</a> to no avail.</p><p><strong>Edit</strong>: And now that I see my question posted, I see that the text is displayed as intended, so apparently it's just the preview that's a mess? I'm going to guess this is just a bug with the preview. Assuming so, maybe there's an OSQA update that fixes this?</p></div><div id="question-tags" class="tags-container tags">markdown osqa</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '16, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jul '16, 14:46</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-54380" class="comments-container"></div><div id="comment-tools-54380" class="comment-tools"></div><div class="clear"></div><div id="comment-54380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54382"></span>

<div id="answer-container-54382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54382-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you're referring to the preview display of your question being messed up by the less than symbol?</p><p>A good way to avoid problems with that is to surround the less-than (and greater than) symbols in back quotes (thus marking it as <code>&lt;code&gt;</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '16, 14:45</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-54382" class="comments-container"><span id="54384"></span><div id="comment-54384" class="comment"><div id="post-54384-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that seems to work with the obvious down-side of <strong>forcing</strong> you to use <code>code</code> for those characters, which you may not really want to do just to appease the previewer.</p><p>But there's another problem - how to get preformatted text (i.e., a text block indented 4 spaces to preview properly? I guess you're forced to use a <code>&lt;code&gt; &lt;/code&gt;</code> block instead and back-tick the characters?</p></div><div id="comment-54384-info" class="comment-info"><span class="comment-age">(27 Jul '16, 16:11)</span> cmaynard ♦♦</div></div><span id="54391"></span><div id="comment-54391" class="comment"><div id="post-54391-score" class="comment-score"></div><div class="comment-text"><p>You can always fall back to good-old HTML escapes &amp;lt; and &amp;gt;</p><p>&lt;Hello Cris&gt;</p></div><div id="comment-54391-info" class="comment-info"><span class="comment-age">(27 Jul '16, 22:31)</span> Jaap ♦</div></div><span id="54398"></span><div id="comment-54398" class="comment"><div id="post-54398-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, thanks. Yes the escape sequences work with inline text or within a <code>&lt;code&gt; &lt;/code&gt;</code> block, but again fail for preformatted text blocks (those indented by 4 spaces) ... mostly.</p><p>If, for example, you attempt to insert tshark -R &lt;Read filter&gt; (here I used escape sequences) within the literal <code>&lt;code&gt; &lt;/code&gt;</code> that I just wrote above, then it fails again. If you add a space following the <code>&lt;</code> character, then it displays properly in the preview.</p></div><div id="comment-54398-info" class="comment-info"><span class="comment-age">(28 Jul '16, 06:21)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-54382" class="comment-tools"></div><div class="clear"></div><div id="comment-54382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


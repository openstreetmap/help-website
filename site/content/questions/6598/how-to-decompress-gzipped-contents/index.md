+++
type = "question"
title = "How to decompress gzipped contents"
description = '''In HTTP request and response, content-encoding is &#x27;gzip&#x27; and content is gzipped. Is there a way to decompress the gzipped content so we can see what the contents are.'''
date = "2011-09-27T09:11:00Z"
lastmod = "2014-08-01T09:39:00Z"
weight = 6598
keywords = [ "gzipped", "content", "decompress" ]
aliases = [ "/questions/6598" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to decompress gzipped contents](/questions/6598/how-to-decompress-gzipped-contents)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6598-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In HTTP request and response, content-encoding is 'gzip' and content is gzipped. Is there a way to decompress the gzipped content so we can see what the contents are.</p></div><div id="question-tags" class="tags-container tags">gzipped content decompress</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '11, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/9ad38567141d9f9faf28c29f850c366a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eusjoji&#39;s gravatar image" /><p>eusjoji<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eusjoji has no accepted answers">0%</span></p></div></div><div id="comments-container-6598" class="comments-container"></div><div id="comment-tools-6598" class="comment-tools"></div><div class="clear"></div><div id="comment-6598-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="12037"></span>

<div id="answer-container-12037" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12037-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe Jaap's answer is not quite correct, because the exported object will already be uncompressed. Since there seems to be some confusion, here are some more explicit steps that should hopefully work for you:</p><ol><li>Find the gzipped object of interest and right-click on the corresponding packet in the packet list, selecting, "Follow TCP Stream" to isolate the stream.</li><li>Within the "Follow TCP Stream" window, note the name of the gzipped object in the previous GET block.</li><li>From the main window, choose File -&gt; Export Objects -&gt; HTTP.</li><li>Select the object. The packet number should match the packet number you discovered in step 1, and the Filename should match the name seen in step 2. Note that the content type that appears is the uncompressed content type, so e.g., text/html, and not gzip.</li><li>Choose Save As, then Save. This will be the uncompressed object.</li></ol><p>Note that you don't necessarily need to do "Follow TCP Stream" as long as you know the packet number and object name of the object of interest, or if you simply want to export all objects.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 18:39</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-12037" class="comments-container"></div><div id="comment-tools-12037" class="comment-tools"></div><div class="clear"></div><div id="comment-12037-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6601"></span>

<div id="answer-container-6601" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6601-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You could export the objects through the file menu and gunzip them offline.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Sep '11, 13:58</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6601" class="comments-container"><span id="6687"></span><div id="comment-6687" class="comment"><div id="post-6687-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Could you specify the detailed procedure on how to do it? Ho wdo I export the objects through the file menu?</p></div><div id="comment-6687-info" class="comment-info"><span class="comment-age">(03 Oct '11, 11:37)</span> eusjoji</div></div><span id="11999"></span><div id="comment-11999" class="comment"><div id="post-11999-score" class="comment-score"></div><div class="comment-text"><p>When exporting did you select the HTML object?</p><p>Also should the gzip show up in the content type in the HTTP object list?</p></div><div id="comment-11999-info" class="comment-info"><span class="comment-age">(17 Jun '12, 15:01)</span> Hig2012</div></div></div><div id="comment-tools-6601" class="comment-tools"></div><div class="clear"></div><div id="comment-6601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35073"></span>

<div id="answer-container-35073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35073-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I made a quick script to convert the Follow TCP Stream output to what you'd expect: <a href="https://github.com/kizzx2/wireshark-http-gunzip">wireshark-http-gunzip</a></p><p>You can use it with a command like this:</p><pre><code>ruby http-gunzip.rb &lt; raw.dump | less</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '14, 09:39</strong></p><img src="https://secure.gravatar.com/avatar/d52fe054646a5a18ed3dbbf90cfae948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kizzx2&#39;s gravatar image" /><p>kizzx2<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kizzx2 has no accepted answers">0%</span></p></div></div><div id="comments-container-35073" class="comments-container"></div><div id="comment-tools-35073" class="comment-tools"></div><div class="clear"></div><div id="comment-35073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


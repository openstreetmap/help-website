+++
type = "question"
title = "Capture filter. TCP stream as txt file"
description = '''Hi guys.  Maybe there is a method, to save or convert wireshark capture file directly to txt? For example, to get the same output into txt file, as we can see, when we press the button &quot;Follow tcp stream&quot; ?'''
date = "2012-06-26T07:24:00Z"
lastmod = "2012-06-26T07:44:00Z"
weight = 12179
keywords = [ "capture", "stream", "tcp" ]
aliases = [ "/questions/12179" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filter. TCP stream as txt file](/questions/12179/capture-filter-tcp-stream-as-txt-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12179-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys.</p><p>Maybe there is a method, to save or convert wireshark capture file directly to txt?</p><p>For example, to get the same output into txt file, as we can see, when we press the button "Follow tcp stream" ?</p></div><div id="question-tags" class="tags-container tags">capture stream tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jun '12, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/f697d55a7a5a16d8e1582edceda33c15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jomajo&#39;s gravatar image" /><p>jomajo<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jomajo has one accepted answer">100%</span></p></div></div><div id="comments-container-12179" class="comments-container"></div><div id="comment-tools-12179" class="comment-tools"></div><div class="clear"></div><div id="comment-12179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12182"></span>

<div id="answer-container-12182" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12182-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use tshark (Version &gt;= 1.7) for that:</p><blockquote><p><code>tshark -r input.cap -R "tcp.stream eq 1" -z follow,tcp,ascii,1</code><br />
</p></blockquote><p>The number is the TCP stream number.</p><p><strong>UPDATE:</strong> You can also try the tshark option -V (all protocol fields "expanded" --&gt; a lot of output").</p><blockquote><p><code>tshark -r input.cap -V "tcp.stream eq 1"</code><br />
</p></blockquote><p>You can combine both options (-V and -z).<br />
</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jun '12, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jun '12, 08:13</p></div></div><div id="comments-container-12182" class="comments-container"><span id="12183"></span><div id="comment-12183" class="comment"><div id="post-12183-score" class="comment-score"></div><div class="comment-text"><p>We can save the capture without opening .cap file at all?</p></div><div id="comment-12183-info" class="comment-info"><span class="comment-age">(26 Jun '12, 07:59)</span> jomajo</div></div><span id="12184"></span><div id="comment-12184" class="comment"><div id="post-12184-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure what you mean by "<strong>save</strong> the capture <strong>without opening</strong> .cap file".</p><p>tshark expects an input file which it opens to extract the data.</p><p>Maybe you can tell me a bit more .....</p></div><div id="comment-12184-info" class="comment-info"><span class="comment-age">(26 Jun '12, 08:01)</span> Kurt Knochner ♦</div></div><span id="12188"></span><div id="comment-12188" class="comment"><div id="post-12188-score" class="comment-score"></div><div class="comment-text"><p>:)</p><p>I am capturing some data. Next day, when I come to check the data, I see few .txt files generated, and when I open these, I can see just tcp stream data ( as you said, ascii characters).</p><p>It would be nice , if it is possible?</p></div><div id="comment-12188-info" class="comment-info"><span class="comment-age">(26 Jun '12, 09:18)</span> jomajo</div></div><span id="12217"></span><div id="comment-12217" class="comment"><div id="post-12217-score" class="comment-score"></div><div class="comment-text"><p>Ah, you want to do it on the fly, without saving the captured data. No, that is not possible with Wireshark or tshark.</p><p>Take a look at <a href="http://www.circlemud.org/jelson/software/tcpflow/">tcpflow</a> (Unix tool)</p><p>BTW: There is a similar <a href="http://ask.wireshark.org/questions/10023/command-line-option-for-follow-tcp-stream">question</a></p></div><div id="comment-12217-info" class="comment-info"><span class="comment-age">(26 Jun '12, 17:02)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-12182" class="comment-tools"></div><div class="clear"></div><div id="comment-12182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "capturing filters from file"
description = '''hi, first of all sorry for my (really) bad english. i was loocking for a way to pass same capturing filters to tshark from a file. i know there is a capturing filters file in $HOME/.config/wireshark/$PROFILE/cfilters, but when i run: (Prova is my PROFILE) tshark -C Prova -c 50 -I -i wlp0s4f1u1 &amp;gt; ...'''
date = "2016-04-13T07:14:00Z"
lastmod = "2016-04-13T09:40:00Z"
weight = 51632
keywords = [ "capture-filters" ]
aliases = [ "/questions/51632" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capturing filters from file](/questions/51632/capturing-filters-from-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51632-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, first of all sorry for my (really) bad english. i was loocking for a way to pass same capturing filters to tshark from a file. i know there is a capturing filters file in $HOME/.config/wireshark/$PROFILE/cfilters, but when i run: (Prova is my PROFILE) tshark -C Prova -c 50 -I -i wlp0s4f1u1 &gt; out.pcap i capture broadcast packets even if i defined a filter to NOT capturing broadcast stuff.</p></div><div id="question-tags" class="tags-container tags">capture-filters</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '16, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/d97312080fe2e4b08aed966178a1c107?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexamico&#39;s gravatar image" /><p>alexamico<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexamico has no accepted answers">0%</span></p></div></div><div id="comments-container-51632" class="comments-container"></div><div id="comment-tools-51632" class="comment-tools"></div><div class="clear"></div><div id="comment-51632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51635"></span>

<div id="answer-container-51635" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51635-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You have to add a name to the capture filter you wish to use and then supply the name to the <code>-f</code> option prefixed with "predef:", e.g. <code>tshark -C Prova -f "predef:MyFilterName" ...</code>.</p><p>See <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8091">Bug 8091</a> and <a href="https://code.wireshark.org/review/#/c/5925/">Change 5925</a> for more information.</p><p>Note this is only available in development builds, i.e. version &gt;= 2.1.x.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '16, 08:02</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Apr '16, 10:05</p></div></div><div id="comments-container-51635" class="comments-container"><span id="51636"></span><div id="comment-51636" class="comment"><div id="post-51636-score" class="comment-score"></div><div class="comment-text"><p>so, if i want to run all and only the filters in $HOME/.config/wireshark/$PROFILE/cfilters i MUST write some sort of script?! there isn't a method to tell tshark to run all and only those filters?</p></div><div id="comment-51636-info" class="comment-info"><span class="comment-age">(13 Apr '16, 08:28)</span> alexamico</div></div><span id="51638"></span><div id="comment-51638" class="comment"><div id="post-51638-score" class="comment-score"></div><div class="comment-text"><p>Nope, you can only pass <strong>one</strong> filter into tshark (and Wireshark for that matter). You can combine multiple filter expressions into a single filter using logical operators, probably with <code>and</code> or <code>&amp;&amp;</code> for your use case.</p><p>You could write a script to read all the filter expressions in cfilters and combine them programmatically and then call tshark.</p></div><div id="comment-51638-info" class="comment-info"><span class="comment-age">(13 Apr '16, 08:36)</span> grahamb ♦</div></div></div><div id="comment-tools-51635" class="comment-tools"></div><div class="clear"></div><div id="comment-51635-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51642"></span>

<div id="answer-container-51642" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51642-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>cfilters</code> file is merely a collection of saved capture filters, but none of those filters are applied automatically. You must explicitly specify the capture filter to use on the <code>tshark</code> command-line.</p><p>That said, if you know the order of the saved capture filters in the <code>cfilters</code> file, you can grab the matching line number of the filter you want using something like follows, and here I'm assuming that the filter you want is the 9th entry in the file:</p><pre><code>tshark -C Prova -c 50 -I -i wlp0s4f1u1 -f &quot;`head -9 cfilters | tail -1 | cut -d &#39;\&quot;&#39; -f 3-`&quot; &gt; out.pcap</code></pre><p>Here's what it does:</p><ul><li><code>head -9 cfilters</code>: This displays the 1st 9 lines of the file.</li><li><code>tail -1</code>: This grabs the last line of the previous 9, thus isolating the line containing the desired capture filter.</li><li><code>cut -d '\"' -f 3-</code>: This discards the name of the filter you gave it, leaving only the capture filter itself. Note: There remains a space that precedes the filter, but this is harmless.</li></ul><p>Another solution, and probably a nicer one, would be to just <code>grep</code> the <code>cfilters</code> file for the unique name of the capture filter you gave it. For example, suppose you have a capture filter named, "FOO", you could do this:</p><pre><code>tshark -C Prova -c 50 -I -i wlp0s4f1u1 -f &quot;`grep -m 1 FOO cfilters | cut -d &#39;\&quot;&#39; -f 3-`&quot; &gt; out.pcap</code></pre><p>Passing the <code>-m 1</code> option to <code>grep</code> ensures that only the 1st filter that matches is returned in the event that there's more than one that contains the same search string.</p><p>With this method, you don't need to know the order of the capture filters in the file, but you do need to know the name of the filter, and you should probably make sure they're all unique; otherwise the search might return an unintended match. If you want more than 1 filter, you can combine them. For example, suppose you want to apply a combined capture filter which comprises the individual capture filters you named "FOO" and "BAR":</p><pre><code>tshark -C Prova -c 50 -I -i wlp0s4f1u1 -f &quot;`grep -m 1 FOO cfilters | cut -d &#39;\&quot;&#39; -f 3-` or `grep -m 1 BAR cfilters | cut -d &#39;\&quot;&#39; -f 3-`&quot; &gt; out.pcap</code></pre><p><strong>EDIT</strong>: The solution that grahamb supplied would be preferred, if available, and if you only wanted to apply a single capture filter. The solution I provided could be useful if capture filter labels are not available though or if you wanted to apply more than 1 capture filter. As grahamb mentioned, if you want to apply <em>all</em> filters from the <code>cfilters</code> file, then it probably makes more sense to script something, likely using some of the ideas presented here.</p><p><strong>EDIT2</strong>: Perhaps a script such as follows is more along the lines of what you're looking for?</p><pre><code>#!/bin/sh

input=cfilters
cfs=
while read line
do
        cf=$(echo &quot;$line&quot; | cut -d &quot;\&quot;&quot; -f 3-)
        if [ ! -z &quot;$cf&quot; ]; then
                if [ ! -z &quot;$cfs&quot; ]; then
                        cfs=&quot;($cfs) or ($cf)&quot;
                else
                        cfs=&quot;$cf&quot;
                fi
        fi
done &lt; &quot;$input&quot;

tshark -C Prova -c 50 -I -i wlp0s4f1u1 -f &quot;$cfs&quot; &gt; out.pcap</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '16, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Apr '16, 10:37</p></div></div><div id="comments-container-51642" class="comments-container"></div><div id="comment-tools-51642" class="comment-tools"></div><div class="clear"></div><div id="comment-51642-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


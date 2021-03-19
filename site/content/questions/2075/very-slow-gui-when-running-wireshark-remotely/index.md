+++
type = "question"
title = "Very slow GUI when running wireshark remotely"
description = '''Start seeing this issue after upgrading wireshark from 0.99.8 to 1.2.6. One problem is the extreme long time it takes to initialize the wireshark (i.e., taking almost an hour to register dissectors, etc), which is kind of resolved by increasing the splash update interval; The other problem is that a...'''
date = "2011-02-01T09:49:00Z"
lastmod = "2011-02-02T07:48:00Z"
weight = 2075
keywords = [ "performance" ]
aliases = [ "/questions/2075" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Very slow GUI when running wireshark remotely](/questions/2075/very-slow-gui-when-running-wireshark-remotely)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2075-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Start seeing this issue after upgrading wireshark from 0.99.8 to 1.2.6. One problem is the extreme long time it takes to initialize the wireshark (i.e., taking almost an hour to register dissectors, etc), which is kind of resolved by increasing the splash update interval; The other problem is that after GUI starts up it's running very slow and always takes a long time to respond to user clicks, makes the GUI unusable.</p><p>This only happens when running wireshark remotely (using SSH over X11). Wireshark is using GTK2.</p><p>Does anyone has suggestion on how to improve the GUI performance? Thanks.</p></div><div id="question-tags" class="tags-container tags">performance</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '11, 09:49</strong></p><img src="https://secure.gravatar.com/avatar/3148db2a3ca8f909be97f9891fab6966?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dxl&#39;s gravatar image" /><p>dxl<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dxl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Feb '11, 09:54</p></div></div><div id="comments-container-2075" class="comments-container"></div><div id="comment-tools-2075" class="comment-tools"></div><div class="clear"></div><div id="comment-2075-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2105"></span>

<div id="answer-container-2105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2105-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I (and my coworkers) had problems when we started using a GTK2-based Wireshark because GTK2 uses anti-aliased fonts and our (very old) X server (in this case Exceed v10) did not support anti-aliased fonts. Once (using Wireshark, of course) I (think I) saw that the X client (in this case Wireshark) was being forced to send characters over the network as images; obviously this used a lot of bandwidth and was horrendously slow.</p><p>The situation can be improved by turning off anti-aliased fonts. Creating a $HOME/.fonts.conf file containing this:</p><pre><code>    &lt;?xml version=&quot;1.0&quot;?&gt;
&lt;!DOCTYPE fontconfig SYSTEM &quot;fonts.dtd&quot;&gt;
&lt;fontconfig&gt;

      &lt;match target=&quot;font&quot;&gt;
          &lt;edit name=&quot;antialias&quot; mode=&quot;assign&quot;&gt;&lt;bool&gt;false&lt;/bool&gt;&lt;/edit&gt;
      &lt;/match&gt;

&lt;/fontconfig&gt;</code></pre><p>on the computer where Wireshark is run (and obviously in the $HOME of the user running Wireshark) can help the situation. I don't think you have to do anything else besides starting Wireshark again. If the change took effect you should notice that the fonts Wireshark (and any other GTK2 application) uses look pretty horrible.</p><p>Some of my coworkers reported good success with this change, but others said it didn't help much. If it doesn't help you, you may want to try another X server. Cygwin has a free one for Windows but you may also be able to get demo versions of Windows-based commercial products (at least to see if it's an X-server problem). Personally, all of my remote (via SSH) Wireshark problems went away when I started using Linux on my desktop (with Windows in a VM).</p><p>[Update] Don't forget to drop by and Accept this answer if it answered your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '11, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Mar '12, 07:04</p></div></div><div id="comments-container-2105" class="comments-container"></div><div id="comment-tools-2105" class="comment-tools"></div><div class="clear"></div><div id="comment-2105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


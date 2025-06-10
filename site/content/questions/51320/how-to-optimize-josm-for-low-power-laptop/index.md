+++
type = "question"
title = "How to optimize josm for low-power laptop?"
description = '''I recently bought a chromebook with an ARM processor (the Asus Flip). I&#x27;m using Crouton to run the xfce in a chroot, to provide a full (lightweight) Linux desktop. Everything is working great, except JOSM. It is painfully laggy, with multiple second delays for every action. Click on menu, wait 2-3 s...'''
date = "2016-08-09T20:52:00Z"
lastmod = "2016-08-11T19:36:00Z"
weight = 51320
keywords = [ "hardware", "josm", "optimization", "arm_cpu" ]
aliases = [ "/questions/51320" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to optimize josm for low-power laptop?](/questions/51320/how-to-optimize-josm-for-low-power-laptop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51320-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-51320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently bought a chromebook with an ARM processor (the Asus Flip). I'm using <a href="https://github.com/dnschneid/crouton">Crouton</a> to run the xfce in a chroot, to provide a full (lightweight) Linux desktop. Everything is working great, <em>except</em> JOSM. It is painfully laggy, with multiple second delays for every action. Click on menu, wait 2-3 sec for it to open. Click on node, wait 1-2 sec for to to be selected. Zoom, wait 4-8 seconds. Pretty much unusable.</p>
<p>I bought this laptop for an upcoming bicycle trip, that I am planing to do lots of mapping with it. Because I specifically bought this laptop for running JOSM it's unusability is quite disappointing.</p>
<p>I'm running JOSM from the latest tested .jar file from the command line, giving it extra RAM, with the -Xmx2048m option. The version in the Ubuntu repositories is very old, so I'm not using that (the building plug-in is not supported!).</p>
<p>The bottleneck might be the CPU. It's Rockchip 1.8GHz Quad-core. Sounds fast to me, but htop reports one of the cores in the mid 90 percent range when zooming, or after downloading fresh data. They remain low at other times, despite lag with other tasks.</p>
<p>RAM usage always remains low. Is there a way to optimize CPU usage? Looking at htop, I seem to have multiple threads running.</p>
<p>Sorry if my question is too specific to my needs, I can make it more applicable to others by asking: <strong>How do I trouble shoot JOSM lag, and optimize performance to mitigate lag?</strong></p>
<p><strong>Update:</strong> I've added Sun/Oracle Java, as per the info from <a href="https://help.openstreetmap.org/users/5179/aseerel4c26">aseerel4c26</a> and <a href="https://help.openstreetmap.org/users/30/rorym">rorym</a> and JOSM is now running very responsively. I'm really happy with the results.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hardware" rel="tag" title="see questions tagged &#39;hardware&#39;">hardware</span> <span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-optimization" rel="tag" title="see questions tagged &#39;optimization&#39;">optimization</span> <span class="post-tag tag-link-arm_cpu" rel="tag" title="see questions tagged &#39;arm_cpu&#39;">arm_cpu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '16, 20:52</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '16, 00:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-51320" class="comments-container">
<span id="51321"></span>
<div id="comment-51321" class="comment">
<div id="post-51321-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sounds more like a bug or incompatibility. Did you already test if the problem persists when using different JOSM versions (stable vs latest), a different JRE (openjdk vs Oracle JDK) or another window manager?</p>
</div>
<div id="comment-51321-info" class="comment-info">
<span class="comment-age">(09 Aug '16, 21:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51343"></span>
<div id="comment-51343" class="comment">
<div id="post-51343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>BTW: There are some reports that Asus Flip runs apps from Google Play store as well. Did you try e.g. Vespucci?</p>
<p>Also tried JOSM on my Raspberry PI 2 (also some ARM chipset) using Oracle JDK 8 via remote ssh session. Although it's a bit sluggish it's not completely unusable, running even on 0.9GHz CPU speed only, though. Oracle JDK can be installed via <code>sudo apt-get install oracle-java8-jdk</code> on Raspbian.</p>
</div>
<div id="comment-51343-info" class="comment-info">
<span class="comment-age">(11 Aug '16, 06:41)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="51357"></span>
<div id="comment-51357" class="comment">
<div id="post-51357-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a>, thanks for the info. Looks like it should be possible, but I like the way I've got it set up at the moment, and don't want to break anything right before my trip. (updates to chromeos can break crouton apparently, and running android apps requires changing chromeos to the dev branch)</p>
<p>I'll mess around with it when I get back, because once I'm back the chromebook won't be my only computer, and if it's out of commision for a bit that'll be fine.</p>
<p>If things work out well with this set up I'll do a Diary post on this chromebook. I should probably do a review either way... we'll see how much enthusiasm I have for that.</p>
</div>
<div id="comment-51357-info" class="comment-info">
<span class="comment-age">(11 Aug '16, 19:36)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-51320" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51320-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51324"></span>

<div id="answer-container-51324" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51324-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What java are you using? I found the open source java to be very very slow for JOSM and noticed a massive speed in JOSM when I switched to the closed source Sun/Oracle java.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '16, 09:39</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-51324" class="comments-container">
<span id="51325"></span>
<div id="comment-51325" class="comment">
<div id="post-51325-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>when I type:</p>
<pre><code>java -version</code></pre>
<p>it outputs:</p>
<pre><code>java version &quot;1.7.0_101&quot;
OpenJDK Runtime Environment (IcedTea 2.6.6) (7u101-2.6.6-0ubuntu0.15.10.1)
OpenJDK Zero VM (build 24.95-b01, interpreted mode)</code></pre>
</div>
<div id="comment-51325-info" class="comment-info">
<span class="comment-age">(10 Aug '16, 10:09)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="51326"></span>
<div id="comment-51326" class="comment">
<div id="post-51326-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That looks like the open source Java. The logo used when JOSM starts will also tell you. I suggest installing, and switching to, the closed source java, it might be much faster.</p>
</div>
<div id="comment-51326-info" class="comment-info">
<span class="comment-age">(10 Aug '16, 10:10)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="51330"></span>
<div id="comment-51330" class="comment">
<div id="post-51330-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9027/keithonearth"></a><a href="http://help.openstreetmap.org/users/9027/keithonearth">@keithonearth</a>: try to update to Java 8. You are running version 7. The next JOSM "tested" release (in a few days) will not run with this old Java version anymore. Small performance improvements are expected, too.</p>
<p>For comparison, this is an example <code>-version</code> output of Java 8 (with openJDK on a x86-64 system):</p>
<pre><code>openjdk version &quot;1.8.0_102&quot;
OpenJDK Runtime Environment (build 1.8.0_102-b14)
OpenJDK 64-Bit Server VM (build 25.102-b14, mixed mode)</code></pre>
</div>
<div id="comment-51330-info" class="comment-info">
<span class="comment-age">(10 Aug '16, 13:01)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51324" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51324-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="51331"></span>

<div id="answer-container-51331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51331-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-51331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It <em>seems</em> (see "Update" below) there is no openJDK VM for ARM processors available which uses (fast) assembler code. See <a href="http://icedtea.classpath.org/wiki/ZeroSharkFaq">http://icedtea.classpath.org/wiki/ZeroSharkFaq</a> "As an interpreter-only port of OpenJDK, Zero is very much slower than vanilla OpenJDK on the same hardware." You seem to run "Zero VM" (see your java version output). Slowness of all Java applications is expected – but at least they run (that's the goal of "Zero"). Other Java applications should run comparatively slow, too.</p>
<p><em>Update:</em> according to <a href="https://en.wikipedia.org/wiki/Comparison_of_Java_virtual_machines#Supported_CPU_architectures">Wikipedia</a>, openJDK looks to be available also without "Zero" for ARM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '16, 13:02</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '16, 01:29</strong> </span></p>
</div>
</div>
<div id="comments-container-51331" class="comments-container">
<span id="51333"></span>
<div id="comment-51333" class="comment">
<div id="post-51333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you! Installing Sun/Oracle Java has improved the performance so that it's faster than on my x86 laptop. It's working beautifully now.</p>
</div>
<div id="comment-51333-info" class="comment-info">
<span class="comment-age">(10 Aug '16, 19:44)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="51342"></span>
<div id="comment-51342" class="comment">
<div id="post-51342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9027/keithonearth"></a><a href="http://help.openstreetmap.org/users/9027/keithonearth">@keithonearth</a>: fine! :-) Could you please provide the <code>java -version</code> output? (just for other people's reference). And I guess the Oracle Java download for ARM was on the official page?</p>
</div>
<div id="comment-51342-info" class="comment-info">
<span class="comment-age">(11 Aug '16, 00:28)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51331-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


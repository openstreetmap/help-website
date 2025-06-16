+++
type = "question"
title = "Josm not working on ubuntu 18.04. Issues launching, issues connecting to the internet."
description = '''I&#x27;ve just done a fresh install of ubuntu 18.04, and installed josm from the standard ubuntu repositories. Josm is not working properly. Initially it was failing to launch, and would return the error. java --version returns: openjdk 10.0.1 2018-04-17 OpenJDK Runtime Environment (build 10.0.1+10-Ubunt...'''
date = "2018-04-28T00:09:00Z"
lastmod = "2018-07-07T04:29:00Z"
weight = 63197
keywords = [ "josm", "openjdk", "java", "18.04", "ubuntu" ]
aliases = [ "/questions/63197" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Josm not working on ubuntu 18.04. Issues launching, issues connecting to the internet.](/questions/63197/josm-not-working-on-ubuntu-1804-issues-launching-issues-connecting-to-the-internet)

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
<span id="post-63197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63197-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-63197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've just done a fresh install of ubuntu 18.04, and installed josm from the standard ubuntu repositories. Josm is not working properly.</p>
<p>Initially it was failing to launch, and would return the error. <code>java --version</code> returns:</p>
<pre><code>openjdk 10.0.1 2018-04-17
OpenJDK Runtime Environment (build 10.0.1+10-Ubuntu-3ubuntu1)
OpenJDK 64-Bit Server VM (build 10.0.1+10-Ubuntu-3ubuntu1, mixed mode)</code></pre>
<p>Then it was starting but was unable to connect to the internet, so couldn't download <em>any</em> data, or upload <em>any</em> changes. The error message provided is:</p>
<pre><code>java.security.InvalidAlgorithmParameterException:the trustAnchors parameter must be non-empty</code></pre>
<p>Any recommendations to fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-openjdk" rel="tag" title="see questions tagged &#39;openjdk&#39;">openjdk</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-18.04" rel="tag" title="see questions tagged &#39;18.04&#39;">18.04</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Apr '18, 00:09</strong></p>
<img src="https://secure.gravatar.com/avatar/f88a467aa884aeb760041004f62448ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="keithonearth&#39;s gravatar image" />
<p><span>keithonearth</span><br />
<span class="score" title="2939 reputation points"><span>2.9k</span></span><span title="56 badges"><span class="badge1">●</span><span class="badgecount">56</span></span><span title="76 badges"><span class="silver">●</span><span class="badgecount">76</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="keithonearth has 3 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '18, 20:18</strong> </span></p>
</div>
</div>
<div id="comments-container-63197" class="comments-container">
&#10;</div>
<div id="comment-tools-63197" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63197-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="63572"></span>

<div id="answer-container-63572" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63572-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-63572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="keithonearth has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "answer" I think is in the discussion <a href="/questions/63197/josm-not-working-on-ubuntu-1804-issues-launching-issues-connecting-to-the-internet?page=1&amp;focusedAnswerId=63198#63198">on this other answer</a>. As <a href="https://help.openstreetmap.org/users/5179/aseerel4c26"></a><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a></a> and <a href="https://help.openstreetmap.org/users/9027/keithonearth"></a><a href="https://help.openstreetmap.org/users/9027/keithonearth">@keithonearth</a></a> found, the problem isn't actually with JOSM itself (or that the JOSM shipped by Ubuntu is too old), but seems to be that Ubuntu broke CACERTS in 18.04. As noted <a href="https://josm.openstreetmap.de/ticket/15851">at JOSM</a>, see <a href="https://bugs.launchpad.net/ubuntu/+source/ca-certificates-java/+bug/1739631">this bug</a> at Ubuntu (and notice there's a release tracker at the top of that). Ignore the JDK version in that bug title, it apparently applies to them all.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '18, 10:43</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '18, 19:39</strong> </span></p>
</div>
</div>
<div id="comments-container-63572" class="comments-container">
<span id="63609"></span>
<div id="comment-63609" class="comment">
<div id="post-63609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> for the the help figuring this out, and summarising the solution with this answer. I'll add some detail to your answer.</p>
<p>I've successfully gotten Josm working on Ubuntu 18.04.</p>
<p>My original issue related to Josm not detecting Java 11, but this seems to been fixed by the developers. At least it wasn't an issue for me after adding the josm repository, and updating.</p>
<p>The second issue was more troublesome.</p>
<p>I followed the workaround described by <a href="https://launchpad.net/~alankila">Antti S. Lankila</a> in <a href="https://bugs.launchpad.net/ubuntu/+source/ca-certificates-java/+bug/1739631">the link you provided</a>. Here's a summery.</p>
<ul>
<li><p>I downgraded to openjdk-8-jdk</p></li>
<li><p>removed the file /etc/ssl/certs/java/cacerts</p></li>
<li><p>ran the command update-ca-certificates -f</p></li>
<li><p>started JOSM, and it worked.</p></li>
</ul>
<p>The instructions I was following recommended, upgrading to openjdk-9, but neither this nor openjdk-10 is provided in the standard repositories, and Josm is not complaining about the old version of Java, so I've left it as openjdk-8-jdk. So far this has not caused any issues.</p>
</div>
<div id="comment-63609-info" class="comment-info">
<span class="comment-age">(22 May '18, 08:26)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="63983"></span>
<div id="comment-63983" class="comment">
<div id="post-63983-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I had the same problem and I followed the summary from keithonearth, even I did'nt downgraded the openjdk, it works ! Thanks a lot.</p>
</div>
<div id="comment-63983-info" class="comment-info">
<span class="comment-age">(03 Jun '18, 18:11)</span> <span class="comment-user userinfo">Guiyou65</span>
</div>
</div>
</div>
<div id="comment-tools-63572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63572-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63198"></span>

<div id="answer-container-63198" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63198-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I guess that JOSM in the standard ubuntu repositories is (way) too old. Which version is it?</p>
<p>JOSM is compatible with Java 10 <a href="https://josm.openstreetmap.de/ticket/15560#comment:26">since</a> version 13520 on 2018-03-12. Uninstall your current JOSM and instead try the current "tested" version of JOSM from the JOSM homepage <a href="https://josm.openstreetmap.de/">https://josm.openstreetmap.de/</a> or add the JOSM repository to your APT system. Also see <a href="https://wiki.openstreetmap.org/wiki/JOSM/Linux#Debian_.28includes_Ubuntu.29">https://wiki.openstreetmap.org/wiki/JOSM/Linux#Debian_.28includes_Ubuntu.29</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '18, 09:20</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Apr '18, 09:20</strong> </span></p>
</div>
</div>
<div id="comments-container-63198" class="comments-container">
<span id="63219"></span>
<div id="comment-63219" class="comment">
<div id="post-63219-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've added the josm apt repository, and now have version 13576 installed. It is booting up from the menu, the command line, and from the jar file. But in all cases it is unable to connect to the internet. I have installed Oracle Java, 8 &amp; 10.</p>
<p>When starting it gives the error <code>java.security.InvalidAlgorithmParameterException:the trustAnchors parameter must be non-empty</code></p>
<p>(I couldn't copy-past the error, so that may contain typos)</p>
<p>Any clues?</p>
</div>
<div id="comment-63219-info" class="comment-info">
<span class="comment-age">(29 Apr '18, 22:21)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="63307"></span>
<div id="comment-63307" class="comment">
<div id="post-63307-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9027/keithonearth"></a><a href="https://help.openstreetmap.org/users/9027/keithonearth">@keithonearth</a>: due to the <code>InvalidAlgorithmParameterException</code> likely your JOSM cannot set up any HTTPS connections which may feel like "unable to connect to the internet". I am not sure why, though. I guess JOSM cannot find the root CA certificates. <a href="https://stackoverflow.com/questions/6784463/error-trustanchors-parameter-must-be-non-empty/25188331#25188331">Some maybe similar issue on stackoverflow</a>. <del>If you persist to have this problem with the version 13520, and it runs in principle, but just gets this error, it is best to open a bug at JOSM - use the integrated JOSM bug reporter.</del> <del>I think this error is fixed in version 13693 (see <a href="https://josm.openstreetmap.de/ticket/15851">ticket 15851</a>). Wait for the release (see don-vip's answer) or use the "latest" version manually.</del> Your current problem is still open - see <a href="https://josm.openstreetmap.de/ticket/15851">ticket 15851</a>.</p>
</div>
<div id="comment-63307-info" class="comment-info">
<span class="comment-age">(04 May '18, 05:31)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="63522"></span>
<div id="comment-63522" class="comment">
<div id="post-63522-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a>, thank you for your comment. I've been checking on the but report every few days, and updating josm-latest from josm's repositories frequently. It's not fixed yet for 18.04, but should be soon.</p>
</div>
<div id="comment-63522-info" class="comment-info">
<span class="comment-age">(16 May '18, 20:28)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="63571"></span>
<div id="comment-63571" class="comment">
<div id="post-63571-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If I'm reading the links correctly then the release tracker is <a href="https://bugs.launchpad.net/ubuntu/+source/ca-certificates-java/+bug/1739631">https://bugs.launchpad.net/ubuntu/+source/ca-certificates-java/+bug/1739631</a> .</p>
</div>
<div id="comment-63571-info" class="comment-info">
<span class="comment-age">(20 May '18, 10:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63584"></span>
<div id="comment-63584" class="comment">
<div id="post-63584-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>! That link was <em>very</em> helpful. I've successfully gotten Josm working for the first time since installing 18.04. I followed the workaround described by <a href="https://launchpad.net/~alankila">Antti S. Lankila</a> in your link. While I've strayed from my original question, and probably should have asked a new question, here is what I did in case it helps someone:</p>
<ul>
<li><p>I downgraded to openjdk-8-jdk</p></li>
<li><p>removed /etc/ssl/certs/java/cacerts</p></li>
<li><p>ran the command update-ca-certificates -f</p></li>
<li><p>started JOSM, and it worked.</p></li>
</ul>
<p>The instructions I was following recommended, upgrading to openjdk-9, but this was not provided in the standard repositories, and Josm is not complaining about the old version of Java, so I've left it as openjdk-8-jdk.</p>
</div>
<div id="comment-63584-info" class="comment-info">
<span class="comment-age">(20 May '18, 20:49)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
<span id="63594"></span>
<div id="comment-63594" class="comment not_top_scorer">
<div id="post-63594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9027/keithonearth"></a><a href="https://help.openstreetmap.org/users/9027/keithonearth">@keithonearth</a> I'd actually suggest that you add that as an answer. I tried to summarise a "correct" answer below but yours has far more detail.</p>
<p>FWIW I suspect (based on what the Ubuntu bug says) that you should be able to go from openjdk 8 back to openjdk 10 after fixing CACERTS.</p>
<p>Edit: Yes, JOSM will run with openjdk 10 after doing this. Also note that <a href="https://josm.openstreetmap.de/ticket/15851">https://josm.openstreetmap.de/ticket/15851</a> is still being updated, monitoring the progress (or lack of it) of the Ubuntu maintainers towards a root cause fix.</p>
</div>
<div id="comment-63594-info" class="comment-info">
<span class="comment-age">(21 May '18, 11:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63610"></span>
<div id="comment-63610" class="comment not_top_scorer">
<div id="post-63610-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another answer seemed unnecessary, seeing as there was nothing wrong with yours, but I added an edited version of my above comment to your answer, and marked your answer correct. I think this will make the solution easy to find, if others come looking.</p>
</div>
<div id="comment-63610-info" class="comment-info">
<span class="comment-age">(22 May '18, 08:29)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-63198" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63198-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63199"></span>

<div id="answer-container-63199" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63199-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The script in /usr/bin/josm is falling to detect the jre from the new 18.04 release. If you run the jar directly it works ok:</p>
<p>java -jar /routetojar/josm.jar</p>
<p>usually /usr/share/josm/josm.jar</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Apr '18, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/c294cf339bcc2cf16329290040bded0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Javier%20Sanchez&#39;s gravatar image" />
<p><span>Javier Sanchez</span><br />
<span class="score" title="70 reputation points">70</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Javier Sanchez has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63199" class="comments-container">
<span id="63569"></span>
<div id="comment-63569" class="comment">
<div id="post-63569-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No, "java -jar /usr/share/josm/josm.jar" does not work on a newly-installed 18.04 system with josm from apt (josm 13576). JOSM gives its confused "proxy" message because it can't retrieve stuff.</p>
</div>
<div id="comment-63569-info" class="comment-info">
<span class="comment-age">(20 May '18, 10:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63199-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63289"></span>

<div id="answer-container-63289" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63289-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The script needed an update to detect Java 10 and 11. This is done in version <a href="https://josm.openstreetmap.de/changeset/13700/josm/">13700</a>.</p>
<p>This version should be released soon (within a week max).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '18, 20:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0daf2db5d576b3fcfbb4f3c0e4c54fa6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="don-vip&#39;s gravatar image" />
<p><span>don-vip</span><br />
<span class="score" title="300 reputation points">300</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="don-vip has 2 accepted answers">33%</span></p>
</div>
</div>
<div id="comments-container-63289" class="comments-container">
<span id="63570"></span>
<div id="comment-63570" class="comment">
<div id="post-63570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to keep this answer up to date, the "trustanchor" issues (see Keithonearth's comment above) still occur and it still doesn't run. Full details at <a href="https://josm.openstreetmap.de/ticket/15851">https://josm.openstreetmap.de/ticket/15851</a> .</p>
</div>
<div id="comment-63570-info" class="comment-info">
<span class="comment-age">(20 May '18, 10:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63289" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63289-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64567"></span>

<div id="answer-container-64567" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64567-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Still waiting on a fix. Still JOSM does not work on Ubuntu 18.04. You can get it to run by running the jar file directly but it cannot connect to the internet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '18, 22:40</strong></p>
<img src="https://secure.gravatar.com/avatar/52fb35fe9a50b36928bdad6a7222bf68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="clickletm&#39;s gravatar image" />
<p><span>clickletm</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="clickletm has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64567" class="comments-container">
<span id="64568"></span>
<div id="comment-64568" class="comment">
<div id="post-64568-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you try the solution provided by SomeoneElse, that I expanded upon?</p>
</div>
<div id="comment-64568-info" class="comment-info">
<span class="comment-age">(07 Jul '18, 04:29)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-64567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64567-form-container" class="comment-form-container">
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


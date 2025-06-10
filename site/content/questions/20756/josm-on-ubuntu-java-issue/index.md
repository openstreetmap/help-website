+++
type = "question"
title = "[closed] Josm on ubuntu - JAVA issue"
description = '''I&#x27;ve installed JOSM with the ubuntu softwarecenter, but it won&#x27;t run. As far as I can tell, I have &quot;OpenJDK Java 7 Runtime&quot; and &quot;IcedTea Java Web Start&quot; installed - and normally don&#x27;t have JAVA issues for the time being. Any magic tricks?'''
date = "2013-03-17T10:50:00Z"
lastmod = "2013-03-18T14:06:00Z"
weight = 20756
keywords = [ "josm", "12.04", "java", "ubuntu" ]
aliases = [ "/questions/20756" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Josm on ubuntu - JAVA issue](/questions/20756/josm-on-ubuntu-java-issue)

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
<span id="post-20756-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20756-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20756-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've installed JOSM with the ubuntu softwarecenter, but it won't run. As far as I can tell, I have "OpenJDK Java 7 Runtime" and "IcedTea Java Web Start" installed - and normally don't have JAVA issues for the time being.</p>
<p>Any magic tricks?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-12.04" rel="tag" title="see questions tagged &#39;12.04&#39;">12.04</span> <span class="post-tag tag-link-java" rel="tag" title="see questions tagged &#39;java&#39;">java</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '13, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/7142ba8e1a5570d498178b1778fb9af9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThorBue&#39;s gravatar image" />
<p><span>ThorBue</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThorBue has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>18 Mar '13, 16:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f7f8127223bd00c9e8f569ce2e9ddf22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RM87&#39;s gravatar image" />
<p><span>RM87</span><br />
<span class="score" title="3346 reputation points"><span>3.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="37 badges"><span class="silver">●</span><span class="badgecount">37</span></span><span title="53 badges"><span class="bronze">●</span><span class="badgecount">53</span></span></p>
</div>
</div>
<div id="comments-container-20756" class="comments-container">
<span id="20757"></span>
<div id="comment-20757" class="comment">
<div id="post-20757-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please explain <em>won't run</em>. Any error messages? OpenJDK should be fine although I don't know if JOSM is ready for Java 7. But you should already have version 6 installed because the Ubuntu josm packages depends on <em>openjdk-6-jre</em>.</p>
</div>
<div id="comment-20757-info" class="comment-info">
<span class="comment-age">(17 Mar '13, 11:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20765"></span>
<div id="comment-20765" class="comment">
<div id="post-20765-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>"won't run" means that nothing happens when trying to start JOSM. No error message. But when trying via terminal I get "No valid JVM found to run JOSM."</p>
<p>I don't have openjdk-6 installed right now, as i'm not sure if having both openjdk-6 &amp; 7 at the same time is possible without conflicts?</p>
</div>
<div id="comment-20765-info" class="comment-info">
<span class="comment-age">(17 Mar '13, 13:28)</span> <span class="comment-user userinfo">ThorBue</span>
</div>
</div>
<span id="20776"></span>
<div id="comment-20776" class="comment">
<div id="post-20776-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What happens exactly when you run <code>java -jar /usr/share/josm/josm.jar</code> in a terminal? Alternatively you can try to download a probably newer version from <a href="http://josm.openstreetmap.de/">http://josm.openstreetmap.de/</a> or try the webstart from the same page.</p>
</div>
<div id="comment-20776-info" class="comment-info">
<span class="comment-age">(17 Mar '13, 16:08)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20780"></span>
<div id="comment-20780" class="comment">
<div id="post-20780-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Running "java -jar /usr/share/josm/josm.jar" gives this</p>
<p>Debian-Release: 0.0.svn4878+dfsg1-1 Build-Date: 2012-02-04 11:37:23 Revision: 4878 Is-Local-Build: true</p>
<p>java.awt.HeadlessException at java.awt.GraphicsEnvironment.checkHeadless(GraphicsEnvironment.java:173) at java.awt.Window.&lt;init&gt;(Window.java:546) at java.awt.Frame.&lt;init&gt;(Frame.java:419) at java.awt.Frame.&lt;init&gt;(Frame.java:384) at javax.swing.JFrame.&lt;init&gt;(JFrame.java:174) at org.openstreetmap.josm.gui.SplashScreen.&lt;init&gt;(SplashScreen.java:42) at org.openstreetmap.josm.gui.MainApplication.main(MainApplication.java:221)</p>
</div>
<div id="comment-20780-info" class="comment-info">
<span class="comment-age">(17 Mar '13, 18:34)</span> <span class="comment-user userinfo">ThorBue</span>
</div>
</div>
</div>
<div id="comment-tools-20756" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20756-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Issue solved" by RM87 18 Mar '13, 16:13

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20782"></span>

<div id="answer-container-20782" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20782-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20782-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20782-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span>@ThorBue</span>: Hm, looks like your Java installation is messed up. Can you run other Java programs? Did you maybe install openjdk-6-jre-headless? You need openjdk-6-jre. Please post the output of "dpkg -l|grep jdk" and "dpkg -l|grep jre", and the output of "java -version".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '13, 22:01</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-20782" class="comments-container">
<span id="20786"></span>
<div id="comment-20786" class="comment">
<div id="post-20786-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have JAVA issues in my browser, that I'm aware of. But it possible that something isn't right as only 2 of the 4 openjdk packages in softwarecenter is installed.</p>
<p><strong>dpkg -l|grep jdk</strong></p>
<pre><code>ii  openjdk-6-jre-headless                 6b27-1.12.3-0ubuntu1~12.04.1                         OpenJDK Java runtime, using Hotspot JIT (headless)
ii  openjdk-6-jre-lib                      6b27-1.12.3-0ubuntu1~12.04.1                         OpenJDK Java runtime (architecture independent libraries)
ii  openjdk-7-jre                          7u15-2.3.7-0ubuntu1~12.04.1                          OpenJDK Java runtime, using Hotspot JIT
ii  openjdk-7-jre-headless                 7u15-2.3.7-0ubuntu1~12.04.1                          OpenJDK Java runtime, using Hotspot JIT (headless)
ii  openjdk-7-jre-lib                      7u15-2.3.7-0ubuntu1~12.04.1                          OpenJDK Java runtime (architecture independent libraries)</code></pre>
<p><strong>dpkg -l|grep jre</strong></p>
<pre><code>ii  default-jre-headless                   1:1.6-43ubuntu2                                      Standard Java or Java compatible Runtime (headless)
ii  icedtea-6-jre-cacao                    6b27-1.12.3-0ubuntu1~12.04.1                         Alternative JVM for OpenJDK, using Cacao
ii  icedtea-6-jre-jamvm                    6b27-1.12.3-0ubuntu1~12.04.1                         Alternative JVM for OpenJDK, using JamVM
ii  icedtea-7-jre-jamvm                    7u15-2.3.7-0ubuntu1~12.04.1                          Alternative JVM for OpenJDK, using JamVM
ii  openjdk-6-jre-headless                 6b27-1.12.3-0ubuntu1~12.04.1                         OpenJDK Java runtime, using Hotspot JIT (headless)
ii  openjdk-6-jre-lib                      6b27-1.12.3-0ubuntu1~12.04.1                         OpenJDK Java runtime (architecture independent libraries)
ii  openjdk-7-jre                          7u15-2.3.7-0ubuntu1~12.04.1                          OpenJDK Java runtime, using Hotspot JIT
ii  openjdk-7-jre-headless                 7u15-2.3.7-0ubuntu1~12.04.1                          OpenJDK Java runtime, using Hotspot JIT (headless)
ii  openjdk-7-jre-lib                      7u15-2.3.7-0ubuntu1~12.04.1                          OpenJDK Java runtime (architecture independent libraries)</code></pre>
<p><strong>java version</strong> "1.6.0_27" OpenJDK Runtime Environment (IcedTea6 1.12.3) (6b27-1.12.3-0ubuntu1~12.04.1) OpenJDK Client VM (build 20.0-b12, mixed mode, sharing)</p>
</div>
<div id="comment-20786-info" class="comment-info">
<span class="comment-age">(18 Mar '13, 06:23)</span> <span class="comment-user userinfo">ThorBue</span>
</div>
</div>
<span id="20787"></span>
<div id="comment-20787" class="comment">
<div id="post-20787-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The <code>openjdk-6-jre</code> package is not installed. Please try to install it and run the command again afterwards.</p>
</div>
<div id="comment-20787-info" class="comment-info">
<span class="comment-age">(18 Mar '13, 07:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="20796"></span>
<div id="comment-20796" class="comment">
<div id="post-20796-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks - after installing openjdk-6 JOSM is working. Guess I thought jdk-6 was an older version, so I didn't install it when i upgraded to 12.04.</p>
</div>
<div id="comment-20796-info" class="comment-info">
<span class="comment-age">(18 Mar '13, 14:06)</span> <span class="comment-user userinfo">ThorBue</span>
</div>
</div>
</div>
<div id="comment-tools-20782" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20782-form-container" class="comment-form-container">
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


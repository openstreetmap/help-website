+++
type = "question"
title = "[closed] Problem with jetty server(stopped) after executing a Java file"
description = '''Hello, I have implemented a Java function in my graphhopper project and I import it in a JSP page, the problem is that: when I go to this JSP page, the page is running and after some second there is an error on the page:&quot;Connection Failed&quot; infact in my shell there is this message: 2014-02-28 16:37:4...'''
date = "2014-02-28T16:00:00Z"
lastmod = "2014-03-13T16:36:00Z"
weight = 31123
keywords = [ "jetty", "graphhopper" ]
aliases = [ "/questions/31123" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Problem with jetty server(stopped) after executing a Java file](/questions/31123/problem-with-jetty-serverstopped-after-executing-a-java-file)

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
<span id="post-31123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31123-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have implemented a Java function in my graphhopper project and I import it in a JSP page, the problem is that: when I go to this JSP page, the page is running and after some second there is an error on the page:"Connection Failed" infact in my shell there is this message:</p>
<pre><code>2014-02-28 16:37:47.648:INFO:oejsl.ELContextCleaner:javax.el.BeanELResolver purged 2014-02-28 16:37:47.649:INFO:oejsh.ContextHandler:stopped o.m.j.p.JettyWebAppContext{/,file:/home/catia/graphhopperLisa/web/src/main/webapp/},file:/home/catia/graphhopperLisa/web/src/main/webapp/ catia@catia:~/graphhopperLisa$</code></pre>
<p>What is the problem? The Java file that I want to start is a Java file that open a XML file and modify it with DOM; the XML file is 26,7 MB.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-jetty" rel="tag" title="see questions tagged &#39;jetty&#39;">jetty</span> <span class="post-tag tag-link-graphhopper" rel="tag" title="see questions tagged &#39;graphhopper&#39;">graphhopper</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '14, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/3be508f311801a447f51a4dab36a0e57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoifil&#39;s gravatar image" />
<p><span>Zoifil</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoifil has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>16 Mar '14, 01:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-31123" class="comments-container">
&#10;</div>
<div id="comment-tools-31123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31123-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Self-answered, closing since accepting own answers is not possible." by aseerel4c26 16 Mar '14, 01:38

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31528"></span>

<div id="answer-container-31528" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31528-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have solved, the problem was in the java file, because I use an System.exit</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '14, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/3be508f311801a447f51a4dab36a0e57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoifil&#39;s gravatar image" />
<p><span>Zoifil</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoifil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-31528" class="comments-container">
&#10;</div>
<div id="comment-tools-31528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31528-form-container" class="comment-form-container">
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


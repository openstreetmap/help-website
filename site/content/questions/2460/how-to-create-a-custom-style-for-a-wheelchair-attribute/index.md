+++
type = "question"
title = "How to create a custom style for a wheelchair attribute"
description = '''Hello, I work as part of a school project on a accessibility map for people that use a wheelchair in Unna (small German town) https://www.openstreetmap.org/?lat=51.53525&amp;amp;lon=7.68865&amp;amp;zoom=16&amp;amp;layers=M . I need to extend the capabilties of osmarender. The goal is to render streets/ways etc. ...'''
date = "2011-01-26T13:39:00Z"
lastmod = "2011-02-09T12:59:00Z"
weight = 2460
keywords = [ "customised", "rendering", "style", "accessibility" ]
aliases = [ "/questions/2460" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a custom style for a wheelchair attribute](/questions/2460/how-to-create-a-custom-style-for-a-wheelchair-attribute)

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
<span id="post-2460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2460-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I work as part of a school project on a accessibility map for people that use a wheelchair in Unna (small German town) <a href="https://www.openstreetmap.org/?lat=51.53525&amp;lon=7.68865&amp;zoom=16&amp;layers=M">https://www.openstreetmap.org/?lat=51.53525&amp;lon=7.68865&amp;zoom=16&amp;layers=M</a> . I need to extend the capabilties of osmarender. The goal is to render streets/ways etc. with the tag wheelchair in red/yellow/green in dependence to its value (no/limited/yes).</p>
<p>I found the way to do so is to customize the rules and styles: My First try was something like:</p>
<pre><code>rule e=&quot;way&quot; k=&quot;highway&quot; v=&quot;*&quot;&gt;
        rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;no&quot;&gt;
          line class=&quot;wheelchair-no&quot;/&gt;
        /rule&gt;
        rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;yes&quot;&gt;
          line class=&quot;wheelchair-yes&quot;/&gt;
        /rule&gt;
        rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;limited&quot;&gt;
          line class=&quot;wheelchair-limited&quot;/&gt;
        /rule&gt;
/rule&gt;</code></pre>
.wheelchair-no { fill: red; stroke: #4D5D73; stroke-width: 1px; }
<pre><code>        .wheelchair-yes {
        fill: green;
        stroke: #4D5D73;
        stroke-width: 1px;
        }
&#10;        .wheelchair-limited {
        fill: yellow;
        stroke: #4D5D73;
        stroke-width: 1px;
        }</code></pre>
<p>If you have an idea how to get it work i would be pleased.</p>
<p>OSM: Dreckschüppengesicht</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-customised" rel="tag" title="see questions tagged &#39;customised&#39;">customised</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-accessibility" rel="tag" title="see questions tagged &#39;accessibility&#39;">accessibility</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Jan '11, 13:39</strong></p>
<img src="https://secure.gravatar.com/avatar/93fc3ae9e713fae5addc0bb6dfc6c1a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Drecksch%C3%BCppengesicht&#39;s gravatar image" />
<p><span>Dreckschüppe...</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dreckschüppengesicht has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '11, 14:11</strong> </span></p>
</div>
</div>
<div id="comments-container-2460" class="comments-container">
&#10;</div>
<div id="comment-tools-2460" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2460-form-container" class="comment-form-container">
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

<span id="2473"></span>

<div id="answer-container-2473" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2473-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2473-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2473-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would use something like this:</p>
<pre><code>&lt;rule e=&quot;way&quot; k=&quot;highway&quot; v=&quot;*&quot;&gt;
    &lt;rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;no&quot; closed=&quot;yes&quot;&gt;
            &lt;area class=&quot;wheelchair-no-area&quot;&gt;
    &lt;/rule&gt;
    &lt;rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;no&quot; closed=&quot;no&quot;&gt;
            &lt;line class=&quot;wheelchair-no&quot; smart-linecap=&quot;no&quot;/&gt;
    &lt;/rule&gt;
&#10;    &lt;rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;yes&quot; closed=&quot;yes&quot;&gt;
            &lt;area class=&quot;wheelchair-yes-area&quot;&gt;
    &lt;/rule&gt;
    &lt;rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;yes&quot; closed=&quot;no&quot;&gt;
            &lt;line class=&quot;wheelchair-yes&quot; smart-linecap=&quot;no&quot;/&gt;
    &lt;/rule&gt;
&#10;    &lt;rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;limited&quot; closed=&quot;yes&quot;&gt;
            &lt;line class=&quot;wheelchair-limited-area&quot;&gt;
    &lt;/rule&gt;
    &lt;rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;limited&quot; closed=&quot;no&quot;&gt;
            &lt;line class=&quot;wheelchair-limited&quot; smart-linecap=&quot;no&quot;/&gt;
    &lt;/rule&gt;
&lt;/rule&gt;
&#10;.wheelchair-no-area {
    fill: #ff0000;
}
&#10;.wheelchair-yes-area {
    fill: #00ff00;
}
&#10;.wheelchair-limited-area {
    fill: #ffff00;
}
&#10;.wheelchair-no {
    fill: none;
    stroke: #ff0000;
    stroke-width: 1px;
    stroke-linecap: round;
}
&#10;.wheelchair-yes {
    fill: none;
    stroke: #00ff00;
    stroke-width: 1px;
    stroke-linecap: round;
}
&#10;.wheelchair-limited {
    fill: none;
    stroke: #ffff00;
    stroke-width: 1px;
    stroke-linecap: round;
}</code></pre>
<p>But unless you say what you exactly want to accieve and what your problem is, it's hard to give helpful advice.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '11, 10:12</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-2473" class="comments-container">
&#10;</div>
<div id="comment-tools-2473" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2473-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2514"></span>

<div id="answer-container-2514" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2514-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2514-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2514-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, thanks for the answere. The main goal is a simple map of the inner area of Unna (Germany).</p>
<p>We did tag nearly every street in the inner circle with wheelchair=yes/no/limited. In the target map these streets should be redered in:</p>
<ul>
<li>green (yes)</li>
<li>red (no)</li>
<li>yellow (limited)</li>
</ul>
<p>At first it worked pretty fine (first post). On a clean checkout of osmareder we did add this few rules and got a more or less nice map. Now it doesn't work any more. I changed the rules to yours and again nothing changed.</p>
<p>In JOSM as I can see there is no problem with the data.</p>
<p>BTW: What is the fastest way to get the map rendered? If there would be a possibility to parallelize it I could use up to 8 64 bit multi core desktops for one a few nights.</p>
<p>bye muebau</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '11, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/2a8fc7b8521e6189dd06ad9710932713?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="muebau&#39;s gravatar image" />
<p><span>muebau</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="muebau has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '11, 14:31</strong> </span></p>
</div>
</div>
<div id="comments-container-2514" class="comments-container">
&#10;</div>
<div id="comment-tools-2514" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2514-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2521"></span>

<div id="answer-container-2521" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-2521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Turns out that it wasn't only an osmarender problem but a problem with rsvg / eye of gnome.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '11, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-2521" class="comments-container">
&#10;</div>
<div id="comment-tools-2521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2521-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2461"></span>

<div id="answer-container-2461" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2461-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2461-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-2461-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found a partitial solution:</p>
<pre><code>    rule e=&quot;way&quot; k=&quot;highway&quot; v=&quot;*&quot;&gt;
        rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;no&quot;&gt;
          line class=&quot;wheelchair-no&quot; smart-linecap=&quot;no&quot;/&gt;
        /rule&gt;
        rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;yes&quot;&gt;
          line class=&quot;wheelchair-yes&quot; smart-linecap=&quot;no&quot;/&gt;
        /rule&gt;
        rule e=&quot;way&quot; k=&quot;wheelchair&quot; v=&quot;limited&quot;&gt;
          line class=&quot;wheelchair-limited&quot; smart-linecap=&quot;no&quot;/&gt;
        /rule&gt;
    /rule&gt;
</code></pre>
<pre><code> .wheelchair-no {
  fill: none;
  stroke: #ff0000;
  stroke-width: 1px;
  stroke-linecap: round;
        }
&#10;.wheelchair-yes {
  fill: none;
  stroke: #00ff00;
  stroke-width: 1px;
  stroke-linecap: round;
        }
&#10;.wheelchair-limited {
  fill: none;
  stroke: #ffff00;
  stroke-width: 1px;
  stroke-linecap: round;
 }</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '11, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/93fc3ae9e713fae5addc0bb6dfc6c1a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Drecksch%C3%BCppengesicht&#39;s gravatar image" />
<p><span>Dreckschüppe...</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dreckschüppengesicht has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2461" class="comments-container">
&#10;</div>
<div id="comment-tools-2461" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2461-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2838"></span>

<div id="answer-container-2838" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2838-score" class="post-score" title="current number of votes">
-4
</div>
<span id="post-2838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>is your map published? Where?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '11, 12:36</strong></p>
<img src="https://secure.gravatar.com/avatar/cb9e3487765b1e13e3fd6ebb00fdcac7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartograefin&#39;s gravatar image" />
<p><span>Kartograefin</span><br />
<span class="score" title="592 reputation points">592</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartograefin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-2838" class="comments-container">
<span id="2843"></span>
<div id="comment-2843" class="comment">
<div id="post-2843-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you want to get extra information from the questioner, you need to do it in a comment to the original question, rather than an answer.</p>
</div>
<div id="comment-2843-info" class="comment-info">
<span class="comment-age">(09 Feb '11, 12:59)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
</div>
<div id="comment-tools-2838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2838-form-container" class="comment-form-container">
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


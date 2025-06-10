+++
type = "question"
title = "extract highway with name"
description = '''Hey all, What I want do is extract a piece of the roadsystem out of an osm file and put it in a csv. This should contain the lat lon for every node belong to that roadsystem, the node id, and the name of the road to where the node belongs. I did some searching on the net and found that I can use osm...'''
date = "2015-10-15T14:01:00Z"
lastmod = "2015-10-19T22:56:00Z"
weight = 45914
keywords = [ "extraction", "osmconvert", "csv", "osmfilter", "highway" ]
aliases = [ "/questions/45914" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [extract highway with name](/questions/45914/extract-highway-with-name)

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
<span id="post-45914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45914-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey all,</p>
<p>What I want do is extract a piece of the roadsystem out of an osm file and put it in a csv. This should contain the lat lon for every node belong to that roadsystem, the node id, and the name of the road to where the node belongs.</p>
<p>I did some searching on the net and found that I can use osmfilter and osmconvert to get the job done. I managed to get the nodeId, the lat and the lon into a csv using the next statements:</p>
<pre><code>./osmfilter test.o5m --keep=&quot;highway=motorway =motorway_link =primary&quot; --drop-ways --drop-relations &gt; highways.osm</code></pre>
<p>to filter the osm file and</p>
<pre><code>./osmconvert highways.osm --csv=&quot;@oname @id @lon @lat&quot; --csv-headline -o=test.csv</code></pre>
<p>On the other hand I also need the names of the road for eacht node. Is there anwy way to do so? thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extraction" rel="tag" title="see questions tagged &#39;extraction&#39;">extraction</span> <span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Oct '15, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/86b47cdcfeb8e17e43b0aa2abc44d98a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jorne&#39;s gravatar image" />
<p><span>Jorne</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jorne has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45914" class="comments-container">
<span id="45924"></span>
<div id="comment-45924" class="comment">
<div id="post-45924-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I have no experience with those tools, but since you drop the ways, I think you lost the name information. You should look for the ways fulfilling your criteria and then take the nodes of those ways. Nodes that are defining a road do not have the attributes you are looking for (name, highway=primary). Those tags are set on the ways.</p>
</div>
<div id="comment-45924-info" class="comment-info">
<span class="comment-age">(16 Oct '15, 06:23)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-45914" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45914-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="46001"></span>

<div id="answer-container-46001" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46001-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not something you will be able to solve without programming skills. You will need to write a little program in a language of your choice that can parse XML documents. Download the area of interest as XML file. You will notice that it consists of three sections - one with all the nodes, one with all the ways, and one with all the relations.</p>
<p>Build your program so that it first reads the nodes, storing the latitude and longitude for each node found. Then, when your program arrives at the ways section, let it check whether the way is indeed a road (could also be a building or a power line or something), and when it is, have your program output the way's nodes together with the (previously recorded) node id.</p>
<p>A very simple Perl program that does this might look like this</p>
<pre><code>#!/usr/bin/perl
while(&lt;&gt;) {
  if (/&lt;node id=&quot;(\d+)&quot; .*lat=&quot;([^&quot;]+)&quot; .*lon=&quot;([^&quot;]+)&quot;/) {
    $loc{$1}=&quot;$2,$3&quot;;
  } elsif(/&lt;tag k=&quot;(.*)&quot; v=&quot;(.*)&quot;/) {
    $hwy = $2 if ($1 eq &quot;highway&quot;);
    $nam = $2 if ($1 eq &quot;name&quot;);
  } elsif(/&lt;nd ref=&quot;(\d+)&quot;/) {
    push(@nodes,$1);
  } elsif(/&lt;\/way/) {
    if (defined($hwy)) {
      printf &quot;%d,\&quot;%s\&quot;,%s\n&quot;, $_, $nam, $loc{$_} foreach(@nodes);
    }
    undef $hwy, $nam, @nodes;
  }
}</code></pre>
<p>Of course there's many ways in which this can be made more resilient and faster if you need to process large amounts of data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '15, 22:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '15, 22:59</strong> </span></p>
</div>
</div>
<div id="comments-container-46001" class="comments-container">
&#10;</div>
<div id="comment-tools-46001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46001-form-container" class="comment-form-container">
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


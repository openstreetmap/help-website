+++
type = "question"
title = "Unable to render tiles after full planet import"
description = '''I want to start my own tile server, I used this manual to set up my machine. And everything is working with a small country. Then I ordered powerful machine and started rendering full planet. db_settings My import command was: command. My import output is: output My database log is: log. As the resu...'''
date = "2017-08-31T10:01:00Z"
lastmod = "2017-09-04T21:34:00Z"
weight = 58887
keywords = [ "import", "renderd", "planet_osm" ]
aliases = [ "/questions/58887" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to render tiles after full planet import](/questions/58887/unable-to-render-tiles-after-full-planet-import)

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
<span id="post-58887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58887-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to start my own tile server, I used this <a href="https://ircama.github.io/osm-carto-tutorials/tile-server-ubuntu/">manual</a> to set up my machine. And everything is working with a small country. Then I ordered powerful machine and started rendering full planet. <a href="https://pastebin.com/Tscvdcbb">db_settings</a> My import command was: <a href="https://pastebin.com/3u6jtTDQ">command</a>. My import output is: <a href="https://pastebin.com/GSg8kUtH">output</a> My database log is: <a href="https://pastebin.com/u7v8ji3w">log</a>. As the result, my renderd doesn't serve tiles and this is its output: <a href="https://pastebin.com/6M227Lza">link</a> I made import twice and got the same result. What did I do wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '17, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/26ad8fe9ec000bd4adde38ae26c76d81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vovakr&#39;s gravatar image" />
<p><span>vovakr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vovakr has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-58887" class="comments-container">
<span id="58967"></span>
<div id="comment-58967" class="comment">
<div id="post-58967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okay, I redid the import. Here is a result: <a href="https://pastebin.com/D3jDUa2E">output</a> There weren't any errors or anything strange. And again nothing works. What is the possible problem?</p>
</div>
<div id="comment-58967-info" class="comment-info">
<span class="comment-age">(04 Sep '17, 15:29)</span> <span class="comment-user userinfo">vovakr</span>
</div>
</div>
<span id="58972"></span>
<div id="comment-58972" class="comment">
<div id="post-58972-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>This seems to be ok now. Please explain in which way "my renderd doesn't serve tiles". When you try and access a tile, does it immediately return an error message, or does it take a while before an error is returned? Or do you get a white or blue tile only? Does /var/lib/mod_tile contain any .meta files in any of the subdirectories?</p>
</div>
<div id="comment-58972-info" class="comment-info">
<span class="comment-age">(04 Sep '17, 21:34)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58887-form-container" class="comment-form-container">
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

<span id="58889"></span>

<div id="answer-container-58889" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58889-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The import was not successful. A successful import will end with a line such as</p>
<pre><code>osm2pgsql took 12,735s overall</code></pre>
<p>But I don't see that in the import <a href="https://pastebin.com/GSg8kUtH">output</a>. Can you investigate what else happened at 2017-08-31 00:48:41 UTC (perhaps, the machine running out of memory?).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '17, 10:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-58889" class="comments-container">
<span id="58892"></span>
<div id="comment-58892" class="comment">
<div id="post-58892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. My machine is AWS t2.2xlarge (8 cores, 32 GB RAM, 1TB SSD) Could you also recommend some changes to my DB configuration? I will add a swap file. What else can I do to ensure in a successful import?</p>
</div>
<div id="comment-58892-info" class="comment-info">
<span class="comment-age">(31 Aug '17, 11:18)</span> <span class="comment-user userinfo">vovakr</span>
</div>
</div>
<span id="58893"></span>
<div id="comment-58893" class="comment">
<div id="post-58893-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I can't help with sizing for a planet import, I'm afraid. There are some benchmarks at <a href="https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks">https://wiki.openstreetmap.org/wiki/Osm2pgsql/benchmarks</a> , but I'd take those with a big pinch of salt - some of them are quite old, when the planet was much smaller.</p>
</div>
<div id="comment-58893-info" class="comment-info">
<span class="comment-age">(31 Aug '17, 12:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="58968"></span>
<div id="comment-58968" class="comment">
<div id="post-58968-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For completeness (and hopefully useful to someone else) your later import says "Osm2pgsql took 174848s overall", which is just over 2 days elapsed.</p>
</div>
<div id="comment-58968-info" class="comment-info">
<span class="comment-age">(04 Sep '17, 15:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-58889" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58889-form-container" class="comment-form-container">
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


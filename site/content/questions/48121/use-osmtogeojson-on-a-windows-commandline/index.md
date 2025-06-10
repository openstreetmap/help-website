+++
type = "question"
title = "Use osmtogeojson on a windows commandline"
description = '''Hi I wish to use osmtogeojson on a windows commandline to convert OSM data. I saw the usage section here (1) but unsure if that&#x27;s relevant to windows. What does the $ signify? Do I need to perform the npm install?  (1): https://github.com/tyrasd/osmtogeojson Edit: I&#x27;ve removed what I previously did ...'''
date = "2016-02-14T16:22:00Z"
lastmod = "2016-02-16T12:50:00Z"
weight = 48121
keywords = [ "windows", "osmtogeojson", "commandline" ]
aliases = [ "/questions/48121" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Use osmtogeojson on a windows commandline](/questions/48121/use-osmtogeojson-on-a-windows-commandline)

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
<span id="post-48121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48121-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I wish to use osmtogeojson on a windows commandline to convert OSM data. I saw the usage section here (1) but unsure if that's relevant to windows. What does the $ signify? Do I need to perform the npm install?</p>
<p>(1): <a href="https://github.com/tyrasd/osmtogeojson">https://github.com/tyrasd/osmtogeojson</a></p>
<p>Edit: I've removed what I previously did as it would just confuse any future readers of this post.</p>
<p>After a lot of head scratching I've finally got it to work, but probably not as intended.</p>
<p>I downloaded &amp; installed <code>node.js</code> Windows installer <a href="https://nodejs.org/en/">https://nodejs.org/en/</a> The file I required was installed at: <code>C:\Program Files\nodejs\node.exe</code></p>
<p>I then downloaded &amp; extracted the full zip file from <a href="https://github.com/tyrasd/osmtogeojson">https://github.com/tyrasd/osmtogeojson</a> although for this operation only the osmtogeojson.js is required.</p>
<p>In the folder that contained my OSM data file (FHRS857en-GB.osm) I created a <code>.cmd</code> file which is a more recent incarnation of Windows batch files.</p>
<p>The .cmd file contains the line:</p>
<pre><code>&quot;C:\Program Files\nodejs\node.exe&quot; &quot;C:\GeoJson\osmtogeojson&quot; FHRS857en-GB.osm &gt; FHRS857en-GB.geojson</code></pre>
<p>"C:\GeoJson\osmtogeojson" points to osmtogeojson.js. The path will need to be amended to suit where the .js file was placed.</p>
<p>The.cmd file can be run by double clicking on it in Windows Exporer or running it from a command line.</p>
<hr />
<p>Supposedly the actual node.js file can be used to preform the same procedure, but I couldn't get it to work.</p>
<p>I'm new to npm &amp; didn't really understand what it does. The usage example at <a href="https://github.com/tyrasd/osmtogeojson">https://github.com/tyrasd/osmtogeojson</a> added to the confusion making it appear the npm command has to be run every time a conversion is performed. Unless you're a developer who wants to keep lots of projects filed neatly &amp; kept up to date I don't see the need for it.</p>
<p>npm doesn't inform you where it's installing its files &amp; creates configuration files that fail to locate the files they're trying to run, and giving the same name to different file types <em>really</em> doesn't help.</p>
<p>Thanks to aseerel4c26 &amp; maxerickson for their help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-osmtogeojson" rel="tag" title="see questions tagged &#39;osmtogeojson&#39;">osmtogeojson</span> <span class="post-tag tag-link-commandline" rel="tag" title="see questions tagged &#39;commandline&#39;">commandline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Feb '16, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Feb '16, 12:53</strong> </span></p>
</div>
</div>
<div id="comments-container-48121" class="comments-container">
<span id="48124"></span>
<div id="comment-48124" class="comment">
<div id="post-48124-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You should use the command <code>npm install -g osmtogeojson</code> to install the command line program. npm does not expect you to download anything beforehand, so no need to specify a path for the install target (I guess depending on how you installed node and npm it may be necessary to specify the path to npm).</p>
<p>The line `'C:\Users_\AppData\Local\Temp\npm-5464-54bc4da9\unpack-056e3c18416e\package.json' is saying that whatever you downloaded does not contain npm package information. I guess based on the name you downloaded something related to <a href="http://tyrasd.github.io/osmtogeojson/,">http://tyrasd.github.io/osmtogeojson/,</a> but that is another way of using the code, from a webpage, and won't necessarily have anything to do with npm.</p>
</div>
<div id="comment-48124-info" class="comment-info">
<span class="comment-age">(14 Feb '16, 17:48)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="48139"></span>
<div id="comment-48139" class="comment">
<div id="post-48139-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>One of the reasons to use npm to install packages is that it will automatically fetch and install any libraries that a script might use. In this case, the script doesn't need any additional libraries, so it is possible to rip the script out of a package and run it directly, but people using node.js will still expect to be able to easily install the script by running the command <code>npm install -g osmtogeojson</code>.</p>
</div>
<div id="comment-48139-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 13:07)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="48140"></span>
<div id="comment-48140" class="comment">
<div id="post-48140-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I've added</p>
<p><a href="https://github.com/tyrasd/osmtogeojson/issues/50">https://github.com/tyrasd/osmtogeojson/issues/50</a></p>
</div>
<div id="comment-48140-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 13:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48141"></span>
<div id="comment-48141" class="comment not_top_scorer">
<div id="post-48141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I'm the dev of osmtogeojson.</p>
<p>Did you manage to get it to run in the end? If so, can you please post the steps you performed to do so? I can probably add these instructions/information to the github repo for other Windows users.</p>
</div>
<div id="comment-48141-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 14:11)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
<span id="48142"></span>
<div id="comment-48142" class="comment">
<div id="post-48142-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I've borrowed a Windows machine to check, the node installer installs itself and npm to the path, so a command like <code>npm install -g osmtogeojson</code> works just as expected, and osmtogeojson is immediately available once that completes. No additional fussing around needed.</p>
</div>
<div id="comment-48142-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 14:22)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="48143"></span>
<div id="comment-48143" class="comment">
<div id="post-48143-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... and there is a (slightly cryptic) Windows section in <a href="https://www.npmjs.com/package/npm">https://www.npmjs.com/package/npm</a></p>
</div>
<div id="comment-48143-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 14:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48144"></span>
<div id="comment-48144" class="comment not_top_scorer">
<div id="post-48144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi tyr_asd</p>
<p>I have got it to work, but I want to double check it's the best way to do it. As I said npm/node is new to me, so I maybe misunderstanding some of it main points.</p>
<p>Do you provide a package of overpass 'stuff' for npm to load? Can you dictate the file names? Having the .js &amp; .cmd files both named 'osmtogeojson' is quite confusing when the command does specify the extension..</p>
</div>
<div id="comment-48144-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 14:49)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="48146"></span>
<div id="comment-48146" class="comment not_top_scorer">
<div id="post-48146-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey Dave. Yes, I chose these file names and now I see that it can be indeed irritating. On the other hand, I've expected that most users would install the CLI tool via via <code>npm -g</code>, so I thought it doesn't matter ;-)</p>
<p>When I come around to it, I'll put the different files in different directories (i.e. "executable" <code>osmtogeojson</code> into <code>bin</code>, compiled library <code>osmtogeojson.js</code> into <code>dist</code>,sources into <code>src</code>)…</p>
</div>
<div id="comment-48146-info" class="comment-info">
<span class="comment-age">(15 Feb '16, 15:37)</span> <span class="comment-user userinfo">tyr_asd</span>
</div>
</div>
<span id="48171"></span>
<div id="comment-48171" class="comment not_top_scorer">
<div id="post-48171-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks tyr_asd, that would clarify things. I would suggest putting a link to NPM Windows download page, but I'm sure they'd move it as soon as you did.</p>
<p>Yes SomeoneElse, cryptic is correct. There's few things NPM need to update on their site such as showing the correct folder it's installed to &amp; linking to the easy to understand download page instead os the DOS style directory listing. It seems a bit ironic that a program to ensure packages are up to date has a convoluted procedure to update itself.</p>
<p>I'll add the procedure I followed shortly.</p>
</div>
<div id="comment-48171-info" class="comment-info">
<span class="comment-age">(16 Feb '16, 12:50)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-48121" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-48121-form-container" class="comment-form-container">
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

<span id="48122"></span>

<div id="answer-container-48122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48122-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Likely the "$" there means the command prompt of a Unix-like system's command line interface (see <a href="https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt">https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt</a> ). And npm is the <a href="https://en.wikipedia.org/wiki/Npm_%28software%29">package manager for Node.js</a>. From what I read, it seems that node.js also runs on Windows, so you should be able to use those commands too (after installing node.js, of course).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Feb '16, 16:39</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Feb '16, 16:41</strong> </span></p>
</div>
</div>
<div id="comments-container-48122" class="comments-container">
&#10;</div>
<div id="comment-tools-48122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48122-form-container" class="comment-form-container">
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

</hr>

</div>

</div>


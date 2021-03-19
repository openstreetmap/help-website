+++
type = "question"
title = "how can I tell which images get downloaded from the site vs images requested by user?"
description = '''I have a capture file and I am able to see images that were downloaded but I am trying to differentiate between images that were on the site itself vs images that the user requested to be downloaded from the site. Is there a way to see which images the user requested to save as opposed to just the o...'''
date = "2015-11-14T06:04:00Z"
lastmod = "2015-11-14T08:41:00Z"
weight = 47602
keywords = [ "images", "downloaded", "saved", "requested" ]
aliases = [ "/questions/47602" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how can I tell which images get downloaded from the site vs images requested by user?](/questions/47602/how-can-i-tell-which-images-get-downloaded-from-the-site-vs-images-requested-by-user)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47602-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture file and I am able to see images that were downloaded but I am trying to differentiate between images that were on the site itself vs images that the user requested to be downloaded from the site. Is there a way to see which images the user requested to save as opposed to just the ones that get downloaded by visiting the site? Thanks</p></div><div id="question-tags" class="tags-container tags">images downloaded saved requested</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '15, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/6f5433730d5dc63a6eb6539fbf34b5ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ccices&#39;s gravatar image" /><p>ccices<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ccices has no accepted answers">0%</span></p></div></div><div id="comments-container-47602" class="comments-container"></div><div id="comment-tools-47602" class="comment-tools"></div><div class="clear"></div><div id="comment-47602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47603"></span>

<div id="answer-container-47603" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47603-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>which images the user requested to save<br />
</p></blockquote><p>A typical browser saves <em>all</em> images to disk, to some directory dedicated to files for temporary use. So you cannot tell whether the user has just viewed an image or "saved" it in terms that they would intentionally press "save" and choose a folder where they would want to put the image file. The http request asking for the image file is exactly the same in both cases.</p><blockquote><p>to differentiate between images that were on the site itself vs images that the user requested to be downloaded<br />
</p></blockquote><p>You can, but not very reliably:<br />
</p><ul><li>you may extract the html code, which you can also see in the capture, into a text editor and find links to images in it, which you then compare to the next html requests' targets,</li><li>you may compare the timestamps of the html requests requesting the html code and requesting the images:<br />
</li><li>if they are close to each other, the images were likely downloaded because the html code contained links to them,</li><li>isolated (in time) requests to download a single image indicate intentional user activity.</li></ul><p>So it may be easier and less time consuming to visit the site and see by your own eyes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '15, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Nov '15, 08:43</p></div></div><div id="comments-container-47603" class="comments-container"><span id="47604"></span><div id="comment-47604" class="comment"><div id="post-47604-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. I am trying to answer the question of whether the user intentionally downloaded the images found in the captured stream. When I export the objects, I see that the html gallery page shows 9 of the 10 images I see in the objects exported. I can't seem to see how the user got the 10th image... Would looking at "referrer" in this case assist me?</p></div><div id="comment-47604-info" class="comment-info"><span class="comment-age">(14 Nov '15, 08:45)</span> ccices</div></div><span id="47605"></span><div id="comment-47605" class="comment"><div id="post-47605-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Would looking at "<a href="https://en.wikipedia.org/wiki/HTTP_referer">referrer</a>" in this case assist me?</p></blockquote><p>Again, not very reliably. In your particular case, if its contents differs between the 10th image and the other 9, it is a hint that the request has been triggered in another way than download of the other 9, but you cannot be 100 % sure what kind of event it was.</p></div><div id="comment-47605-info" class="comment-info"><span class="comment-age">(14 Nov '15, 08:59)</span> sindy</div></div></div><div id="comment-tools-47603" class="comment-tools"></div><div class="clear"></div><div id="comment-47603-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


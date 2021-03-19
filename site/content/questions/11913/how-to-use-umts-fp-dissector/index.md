+++
type = "question"
title = "How to use umts-fp dissector?"
description = '''I have a fp packet ,but I don&#x27;t know how to use the umts-fp dissector to disset it . Becouse if I use &quot;fp&quot; filter to filter my packet,then is nothing. Hope the master give advice or comments please! or give me the packet that can be filter by the &quot;fp&quot;.My email is &quot;chenwei0304@163.com&quot;. Thanks!'''
date = "2012-06-14T20:59:00Z"
lastmod = "2012-06-20T18:44:00Z"
weight = 11913
keywords = [ "fp", "umts-fp" ]
aliases = [ "/questions/11913" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to use umts-fp dissector?](/questions/11913/how-to-use-umts-fp-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11913-score" class="post-score" title="current number of votes">0</div><span id="post-11913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a fp packet ,but I don't know how to use the umts-fp dissector to disset it . Becouse if I use "fp" filter to filter my packet,then is nothing.</p><p>Hope the master give advice or comments please! or give me the packet that can be filter by the "fp".My email is "<span class="__cf_email__" data-cfemail="6b08030e051c0e025b585b5f2b">[email protected]</span><a href="http://163.com">163.com</a>".</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fp" rel="tag" title="see questions tagged &#39;fp&#39;">fp</span> <span class="post-tag tag-link-umts-fp" rel="tag" title="see questions tagged &#39;umts-fp&#39;">umts-fp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '12, 20:59</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p><span>smilezuzu</span><br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-11913" class="comments-container"></div><div id="comment-tools-11913" class="comment-tools"></div><div class="clear"></div><div id="comment-11913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11914"></span>

<div id="answer-container-11914" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11914-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11914-score" class="post-score" title="current number of votes">0</div><span id="post-11914-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="smilezuzu has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://wiki.wireshark.org/FP">http://wiki.wireshark.org/FP</a></p><blockquote><h2 id="wireshark">Wireshark</h2><p><br />
The FP dissector is mostly functional, but can currently only be invoked while reading Catapult DCT2000 or Tektronix K12 format traces (these contain the additional information needed in order to properly decode the frames). It would be possible, but challenging, to decode the RRC messages describing the configuration of the lower layers, and use this information to infer how each FP frame should be decoded.</p></blockquote><p>In 1.8.rc1 and trunk if the NBAP signaling is present, you get some of the FP frames dissected. It should also be possible to design an UAT or a new GUI menu to manually enter the data needed and the IP port combination used for a certain FP flow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '12, 21:28</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jun '12, 21:48</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11914" class="comments-container"><span id="12038"></span><div id="comment-12038" class="comment"><div id="post-12038-score" class="comment-score"></div><div class="comment-text"><p>I want to use a GUI to manually enter the preference which need in FP decoding. But I don't know how to add a dialog in wireshark. could you give me some advise？ Thanks!</p></div><div id="comment-12038-info" class="comment-info"><span class="comment-age">(18 Jun '12, 19:32)</span> <span class="comment-user userinfo">smilezuzu</span></div></div><span id="12039"></span><div id="comment-12039" class="comment"><div id="post-12039-score" class="comment-score"></div><div class="comment-text"><p>Hi, I'm interested in this feature as well so it would be good if you open a bug report at <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a> with this feature request so colaboration is possible. I think using an UAT, (see packet-user_encap.c and others) is one option or a completly new GUI menu. But an UAT is perhaps easier as prof of concept. But a Bug report or moving to the developers mailing list is the next step I think.</p></div><div id="comment-12039-info" class="comment-info"><span class="comment-age">(18 Jun '12, 20:52)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="12093"></span><div id="comment-12093" class="comment"><div id="post-12093-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply! could you tell me how to use a UAT.or some information about UAT.</p></div><div id="comment-12093-info" class="comment-info"><span class="comment-age">(20 Jun '12, 18:44)</span> <span class="comment-user userinfo">smilezuzu</span></div></div></div><div id="comment-tools-11914" class="comment-tools"></div><div class="clear"></div><div id="comment-11914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


+++
type = "question"
title = "Distributing a plugin with Wireshark without releasing the source"
description = '''I&#x27;ve looked over the GPL2 and I&#x27;m not sure I understand it in relation to an issue.  We would like to give a binary version of our plugin for free to use at different sites in related organizations. Would building the unmodified release Wireshark with the plugin and then distributing it run afoul of...'''
date = "2014-03-11T09:19:00Z"
lastmod = "2014-03-11T10:00:00Z"
weight = 30685
keywords = [ "gpl", "license", "plugin" ]
aliases = [ "/questions/30685" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Distributing a plugin with Wireshark without releasing the source](/questions/30685/distributing-a-plugin-with-wireshark-without-releasing-the-source)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30685-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've looked over the GPL2 and I'm not sure I understand it in relation to an issue.<br />
</p><p>We would like to give a binary version of our plugin for free to use at different sites in related organizations. Would building the unmodified release Wireshark with the plugin and then distributing it run afoul of the license?</p><p>We wouldn't be charging for Wireshark or the plugin. We wouldn't be changing the Wireshark source code. We don't want to release the source code for the plugin for reasons outside of copyright/patents.</p></div><div id="question-tags" class="tags-container tags">gpl license plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '14, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/0b4ddeb095ff16e8a84fe92d03bbdef4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tlann&#39;s gravatar image" /><p>tlann<br />
<span class="score" title="76 reputation points">76</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tlann has 4 accepted answers">100%</span> </br></p></div></div><div id="comments-container-30685" class="comments-container"><span id="30691"></span><div id="comment-30691" class="comment"><div id="post-30691-score" class="comment-score"></div><div class="comment-text"><p>Define "related organizations". Are they part of your organization, such as wholly owned subsidiaries, or do you mean <em>other</em> organizations but in a related field? If they're other organizations, then if you give any of them your plugin you also have to make the source code of your plugin available upon request, to <em>anyone</em>.</p></div><div id="comment-30691-info" class="comment-info"><span class="comment-age">(11 Mar '14, 11:05)</span> Hadriel</div></div></div><div id="comment-tools-30685" class="comment-tools"></div><div class="clear"></div><div id="comment-30685-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30687"></span>

<div id="answer-container-30687" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30687-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As far as I understand, distributing it inside your company is ok. To other companies is not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Mar '14, 10:00</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-30687" class="comments-container"><span id="30689"></span><div id="comment-30689" class="comment"><div id="post-30689-score" class="comment-score"></div><div class="comment-text"><p>The GPL FAQ discusses distribution and the extent thereof as regards source availability <a href="https://www.gnu.org/licenses/gpl-faq.html#GPLRequireSourcePostedPublic">here</a>. It's not clear to me what the limits are of any specific "organisation".</p></div><div id="comment-30689-info" class="comment-info"><span class="comment-age">(11 Mar '14, 10:47)</span> grahamb ♦</div></div><span id="30692"></span><div id="comment-30692" class="comment"><div id="post-30692-score" class="comment-score"></div><div class="comment-text"><p>IANAL (of course) but the way I've always thought of it (which I think simplifies things greatly) is: GPL requires that you give the source code to anyone you give the binary to. If I give a binary to users in my company then they must be able to get the source if they want it (this is easy as we're in the same company). If I give the binary to someone at another company then I must give the source to those people. If I somehow make the binary public then I must give the source code to everyone because, as they say, the cat's out of the bag.</p></div><div id="comment-30692-info" class="comment-info"><span class="comment-age">(11 Mar '14, 11:15)</span> JeffMorriss ♦</div></div><span id="30693"></span><div id="comment-30693" class="comment"><div id="post-30693-score" class="comment-score"></div><div class="comment-text"><p>IANAL either, but I believe technically if you give it to <em>anyone</em> outside your organization, then <em>anyone</em> must be able to get the source. The license is transferable, so anyone else could get it indirectly from the party you gave it to, and rightly demand the source from you. Or at least that's my interpretation of <a href="https://www.gnu.org/licenses/gpl-faq.html#WhatDoesWrittenOfferValid">this</a>.</p></div><div id="comment-30693-info" class="comment-info"><span class="comment-age">(11 Mar '14, 11:40)</span> Hadriel</div></div><span id="30694"></span><div id="comment-30694" class="comment"><div id="post-30694-score" class="comment-score"></div><div class="comment-text"><p>Right, makes sense. So within my company I can control it because I can prevent it from leaving the "building." Once it's outside of my "control" (so much as I control anything at work ;-)) it's open to the world.</p></div><div id="comment-30694-info" class="comment-info"><span class="comment-age">(11 Mar '14, 12:51)</span> JeffMorriss ♦</div></div><span id="30714"></span><div id="comment-30714" class="comment"><div id="post-30714-score" class="comment-score"></div><div class="comment-text"><p>@Hadriel,</p><p>IANAL either.</p><p>The GPL FAQ seems to imply the requirement to give the source to anybody who asks depends on how you distribute the source in the first place, see the entry about the <a href="https://www.gnu.org/licenses/gpl-faq.html#WhatDoesWrittenOfferValid">written offer of sources</a>.</p><p>If you give the source to the recipients with the binaries, then I think you're done as it's then the recipients duty to make the source available to anyone they distribute the binaries to.</p><p>If however, you only make the offer of sources, then as any third party could obtain the binaries via a further distribution, your offer must be available to that third party, i.e. anyone.</p></div><div id="comment-30714-info" class="comment-info"><span class="comment-age">(12 Mar '14, 02:58)</span> grahamb ♦</div></div><span id="30735"></span><div id="comment-30735" class="comment not_top_scorer"><div id="post-30735-score" class="comment-score"></div><div class="comment-text"><p>Yup good point, but I was assuming tian's question meant he didn't want to distribute the source with the plugin.</p></div><div id="comment-30735-info" class="comment-info"><span class="comment-age">(12 Mar '14, 08:47)</span> Hadriel</div></div><span id="30744"></span><div id="comment-30744" class="comment not_top_scorer"><div id="post-30744-score" class="comment-score"></div><div class="comment-text"><p>Just one more comment: I remember reading recently (but I don't have the time to find the link) that while you cannot give your GPL code to a customer under NDA (i.e., to prevent them from distributing your work) it <em>is</em> possible to "prevent" them from distributing your work by threat of terminating support or whatever. They are (by GPL) still legally allowed to distribute your work (including source code) but you also would have the right to cancel their support agreement if they do. The FSF weighed in on that and agreed it was legal--the GPL says nothing about other contracts that might be in place between the program author and program user.</p></div><div id="comment-30744-info" class="comment-info"><span class="comment-age">(12 Mar '14, 15:26)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-30687" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-30687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


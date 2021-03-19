+++
type = "question"
title = "how to decode Vodafone Diameter specific AVP 260 &amp; 261 using wireshark."
description = '''Hi, I wanted to decode my wireshark to decode the Vodafone Diameter specific AVPs 260 &amp;amp; 261. My wireshark is installed on my Linux Box running with CentOS. I can see the following lie is already added in dictionary.xml [path: /usr/share/wireshark/diameter] &amp;lt;vendor vendor-id=&quot;Vodafone&quot; code=&quot;1...'''
date = "2011-04-19T15:44:00Z"
lastmod = "2011-04-20T15:25:00Z"
weight = 3623
keywords = [ "diameter", "avp", "vodafone" ]
aliases = [ "/questions/3623" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to decode Vodafone Diameter specific AVP 260 & 261 using wireshark.](/questions/3623/how-to-decode-vodafone-diameter-specific-avp-260-261-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3623-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3623-score" class="post-score" title="current number of votes">0</div><span id="post-3623-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I wanted to decode my wireshark to decode the Vodafone Diameter specific AVPs 260 &amp; 261. My wireshark is installed on my Linux Box running with CentOS.</p><p>I can see the following lie is already added in dictionary.xml [path: /usr/share/wireshark/diameter]</p>&lt;vendor vendor-id="Vodafone" code="12645" name="Vodafone"/&gt;<h1 id="and-i-have-added-following-in-the-dictionary.xml">And I have added following in the dictionary.xml:</h1><pre><code>           &lt;avp name=&quot;Radio-Access-Technology&quot; code=&quot;260&quot; vendor-bit=&quot;Vodafone&quot;&gt;
                    &lt;type type-name=&quot;Enumerated&quot;/&gt;
                    &lt;enum name=&quot;UTRAN&quot; code=&quot;1&quot;/&gt;
                    &lt;enum name=&quot;GERAN&quot; code=&quot;2&quot;/&gt;
                    &lt;enum name=&quot;WLAN&quot; code=&quot;3&quot;/&gt;
                    &lt;enum name=&quot;GAN&quot; code=&quot;4&quot;/&gt;
                    &lt;enum name=&quot;HSPA Evolution&quot; code=&quot;5&quot;/&gt;
                    &lt;enum name=&quot;EUTRAN&quot; code=&quot;6&quot;/&gt;
            &lt;/avp&gt;

            &lt;avp name=&quot;Reporting-Reason&quot; code=&quot;261&quot; vendor-bit=&quot;Vodafone&quot;&gt;
                    &lt;type type-name=&quot;Enumerated&quot;/&gt;
                    &lt;enum name=&quot;THRESHOLD&quot; code=&quot;0&quot;/&gt;
                    &lt;enum name=&quot;FINAL&quot; code=&quot;2&quot;/&gt;
                    &lt;enum name=&quot;QUOTA_EXHAUSTED&quot; code=&quot;3&quot;/&gt;
                    &lt;enum name=&quot;VALIDITY_TIME&quot; code=&quot;4&quot;/&gt;
                    &lt;enum name=&quot;OTHER_QUOTA_TYPE&quot; code=&quot;5&quot;/&gt;
                    &lt;enum name=&quot;RATING_CONDITION_CHANGE&quot; code=&quot;6&quot;/&gt;
                    &lt;enum name=&quot;FORCED_REAUTHORISATION&quot; code=&quot;7&quot;/&gt;
            &lt;/avp&gt;</code></pre><p>Still these AVPs are not decoded. Please let me know what is missed here.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-avp" rel="tag" title="see questions tagged &#39;avp&#39;">avp</span> <span class="post-tag tag-link-vodafone" rel="tag" title="see questions tagged &#39;vodafone&#39;">vodafone</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '11, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/5edcb417f6ec8bf11e63a8f619d51ebe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunil&#39;s gravatar image" /><p><span>sunil</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunil has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '12, 22:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3623" class="comments-container"></div><div id="comment-tools-3623" class="comment-tools"></div><div class="clear"></div><div id="comment-3623-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3654"></span>

<div id="answer-container-3654" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3654-score" class="post-score" title="current number of votes">2</div><span id="post-3654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sunil has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try this format instead(Note the part vendor-id="TGPP"): &lt;avp name="GBA-UserSecSettings" code="400" vendor-bit="must" may-encrypt="no" vendor-id="TGPP"&gt; &lt;type type-name="OctetString"/&gt; &lt;/avp&gt;</p><p>There are other examples in the file. Regards Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Apr '11, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-3654" class="comments-container"><span id="3662"></span><div id="comment-3662" class="comment"><div id="post-3662-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Anders. it works.</p></div><div id="comment-3662-info" class="comment-info"><span class="comment-age">(20 Apr '11, 14:00)</span> <span class="comment-user userinfo">sunil</span></div></div><span id="3663"></span><div id="comment-3663" class="comment"><div id="post-3663-score" class="comment-score">1</div><div class="comment-text"><p>Since Anders' suggestion works, you should accept his answer, since that will remove this question from the list of "unanswered" questions.</p></div><div id="comment-3663-info" class="comment-info"><span class="comment-age">(20 Apr '11, 15:25)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-3654" class="comment-tools"></div><div class="clear"></div><div id="comment-3654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>


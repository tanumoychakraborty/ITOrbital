package com.data.collection.sample.data_collection;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class TwitterDTO {

	private String companyName;
	private Long id;
	private String status;
	private Map<Long,CommentDTO> comments = new HashMap<Long,CommentDTO>();
	private int retweets = 0;
	private int liked = 0;
	
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public String getStatus() {
		return status;
	}
	public void setStatus(String status) {
		status = status.replaceAll("\\r|\\n", "");
		this.status = status.trim();
	}
	public Collection<CommentDTO> getComments() {
		return comments.values();
	}
	public void setComment(Long id, CommentDTO comment) {
		this.comments.put(id, comment);
	}
	public int getRetweets() {
		return retweets;
	}
	public String getCompanyName() {
		return companyName;
	}
	public void setCompanyName(String companyName) {
		this.companyName = companyName;
	}
	public void setRetweets(int retweets) {
		this.retweets = retweets;
	}
	public int getLiked() {
		return liked;
	}
	public void setLiked(int liked) {
		this.liked = liked;
	}
	
}

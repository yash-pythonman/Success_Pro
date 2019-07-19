import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowdataComponent } from './showdata.component';

describe('ShowdataComponent', () => {
  let component: ShowdataComponent;
  let fixture: ComponentFixture<ShowdataComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShowdataComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShowdataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
